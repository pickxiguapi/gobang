from tkinter import *
import tkinter as tk
import tkinter.messagebox
from Record_and_GameTree import StepRecordChessBoard
import threading
from tcp_connect import TCPConnect
import time

# 用正则表达式判断字符串是否是合法的IP地址
def isIP(str):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(str):
        return True
    else:
        return False

class CheckerBoardView(tk.Tk, object):
    # 这个类中包含了显示棋盘和棋子的方法
    def __init__(self):
        super(CheckerBoardView, self).__init__()
        # 一些状态属性
        self.allphoto = []
        self.count = 0
        self.can_start = False

        # 初始化棋盘状态
        self.step_record_chess_board = StepRecordChessBoard(1, 1)

        # 绘制棋盘
        self.build_board()
        # 网络模块所需参数的初始化
        self.tcp_control = TCPConnect()
        self.cond = threading.Condition()
        self.color = '1'  # 黑色
        self.proi = '1'  # 先手
        self.is_our_side = True   # 是否为本方回合
        self.is_room_owner = True    # 是否是房主
        self.my_color = 'Black'    # 记录颜色
        self.other_color = 'White'

    def endgame_result(self):
        self.tcp_control.gameStart = False

    def build_board(self):
        def buttonCallBack():
            # 开始游戏
            # 初始化棋盘图形对象
            if self.can_start:
                if self.is_room_owner:
                    self.tcp_control.gameStart = True
                    if len(self.allphoto) > 0:
                        for i in self.allphoto:
                            self.board.delete(i)
    
                    self.allphoto.clear()
                else:
                    tk.messagebox.showinfo('提示', '请等待房主开始游戏')
            else:
                tk.messagebox.showinfo('提示', '请先加入房间或建立房间')

        self.title("五子棋-双人联机")
        self.resizable(width=False, height=False)
        self.board = Canvas(self, bg="#FFFFF0", width=720, height=630)

        # 创建棋盘划线
        for c in range(40, 610, 30):
            x0, y0, x1, y1 = c, 40, c, 580
            self.board.create_line(x0, y0, x1, y1)
        for r in range(40, 610, 30):
            x0, y0, x1, y1 = 40, r, 580, r
            self.board.create_line(x0, y0, x1, y1)

        # 创建棋盘中的辅助数字标签，标定棋盘中线的位置序号1-19
        x0 = 30
        y0 = 5
        for i in range(1, 20):
            tk.Label(self.board, text=i, bg="#FFFFF0").place(x=x0, y=y0)
            x0 += 30
        x0 = 5
        y0 = 30
        for i in range(1, 20):
            tk.Label(self.board, text=i, bg="#FFFFF0").place(x=x0, y=y0)
            y0 += 30

        # 棋盘上功能按钮
        Button(self.board, text="开始游戏", bg="white", activebackground="Black", command=buttonCallBack).place(x=610, y=500)

        '''
        以下关于多人联机的通信
        '''
        # 创建IP显示和输入的文本框
        ip_text = tk.Entry(self.board, bg='white', bd=3, width=13)
        ip_text.insert(0, '请在这里输入IP')
        ip_text.place(x=590, y=200)
        # 创建颜色按钮
        the_color = tk.Button(self.board, text='本方黑色', bg="white", activebackground="Black", command=lambda: self.setcolor(the_color))
        the_color.place(x=610, y=100)
        # 创建先手按钮
        the_proi = tk.Button(self.board, text='本方先手', bg="white", activebackground="Black", command=lambda: self.setproi(the_proi))
        the_proi.place(x=610, y=150)
        # 创建建立房间的按钮，并设置信号量
        create_room = tk.Button(self.board, text='建立房间', bg="white", activebackground="Black", command=lambda: self.create(ip_text))
        create_room.place(x=610, y=250)
        # 创建加入房间的按钮，并设置信号量
        join_room = tk.Button(self.board, text='加入房间', bg="white", activebackground="Black", command=lambda: self.join(ip_text, the_color, the_proi))
        join_room.place(x=610, y=300)

        # 建立事件响应
        self.board.bind("<Button-1>", self.human)
        self.board.pack()

    # 响应本方的下棋事件
    def human(self, event):
        if self.tcp_control.gameStart:
            if self.is_our_side:  # 仅本方回合可以下棋
                self.is_our_side = False
                # 读取鼠标坐标，event_x为横坐标，event_y为纵坐标
                mouse_x = event.x
                mouse_y = event.y
                if 590 > mouse_x > 30 and 590 > mouse_y > 30:
                    # 由鼠标坐标计算并四舍五入出实际的位置坐标（1,1）-（19,19）
                    # 为方便计算设为（0,0）-（18,18）
                    position_x = round((mouse_x - 40) / 30)
                    position_y = round((mouse_y - 40) / 30)
                    # 将二维位置坐标转化为一维动作，方便之后使用，总共有19*19种动作情况
                    # 即对应动作值action范围为0-360
                    action = position_x + 19 * position_y

                    # 棋盘坐标转换
                    y = (action // 19) * 30 + 40
                    x = (action % 19) * 30 + 40

                    if self.step_record_chess_board.has_record(position_x, position_y) == 0:
                        self.step_record_chess_board.insert_record(position_x, position_y)  # 在棋盘中插入该棋子
                        self.step_record_chess_board.insert_position_list(1, (position_x, position_y))
                        self.board.create_oval(x - 14, y - 14, x + 14, y + 14, fill=self.my_color)

                result = self.step_record_chess_board.check_victory()  # 判断是否胜利
                print(result)

                self.count += 1    # 棋子数加1

                # 转换为string类型
                win = str(result)
                piece_num = str(self.count)
                str_x = str(position_x)
                str_y = str(position_y)

                time.sleep(0.2)

                self.tcp_control.send_game_data(self.cond, win, piece_num, str_x, str_y)


                if result == 1 and self.my_color == 'Black':
                    # 解除鼠标左键绑定
                    self.unbind('<Button-1>')
                    tk.messagebox.showinfo('提示', '本方获胜！')
                    self.endgame_result()
                elif result == 0 and self.my_color == 'White':
                    self.unbind('<Button-1>')
                    tk.messagebox.showinfo('提示', '本方获胜！')
                    self.endgame_result()
                else:
                    pass

                callback_human = threading.Thread(target=self.other_human)
                callback_human.start()
            else:
                tk.messagebox.showinfo('提示', '现在是对方回合')
        else:
            tk.messagebox.showinfo('提示', '游戏还未开始')

    # 用于获取对方的数据
    def other_human(self):
        while True:
            game_data = self.tcp_control.get_game_data()
            if game_data[0:1] == '3':
                break

        self.is_our_side = True
        head, win, piece_num, str_x, str_y = game_data.split('#')


        if win == '1' and self.other_color == 'Black':
            # 解除鼠标左键绑定
            self.unbind('<Button-1>')
            tk.messagebox.showinfo('提示', '对方获胜！')
            self.endgame_result()
        elif win == '0' and self.other_color == 'White':
            self.unbind('<Button-1>')
            tk.messagebox.showinfo('提示', '对方获胜！')
            self.endgame_result()
        else:
            pass
        self.count = int(piece_num)
        position_x = int(str_x)
        position_y = int(str_y)

        action = position_x + 19 * position_y

        # 棋盘坐标转换
        y = (action // 19) * 30 + 40
        x = (action % 19) * 30 + 40

        if self.step_record_chess_board.has_record(position_x, position_y) == 0:
            self.step_record_chess_board.insert_record(position_x, position_y)  # 在棋盘中插入该棋子
            self.step_record_chess_board.insert_position_list(1, (position_x, position_y))
            self.board.create_oval(x - 14, y - 14, x + 14, y + 14, fill=self.other_color)

    # 创建房间
    def create(self, text_control):
        if self.tcp_control.flag:  # 不可重新触发
            tk.messagebox.showinfo('提示', '已经加入了房间！')
            return
        self.is_room_owner = True  # 记录是否是房主
        self.can_start = True

        text_control.delete(0, END)
        text_control.insert(0, self.tcp_control.get_my_ip())    # 获取本机IP

        thread_create = threading.Thread(target=self.tcp_control.create_room, args=(self.cond,))    # 创建房间并进入循环
        thread_create.daemon = True  # 设置为守护进程
        thread_create.start()

        thread_pre_data = threading.Thread(target=self.tcp_control.send_pre_data, args=(self.cond, self.color, self.proi))    # 发送游戏准备数据
        thread_pre_data.start()

        print(self.tcp_control.get_game_data())

        if self.proi == '0':
            callback_human = threading.Thread(target=self.other_human)
            callback_human.start()

    # 加入游戏
    def join(self, text, setcolor, setproi):
        if self.tcp_control.flag:  # 不可重新触发
            tk.messagebox.showinfo('提示', '已经建立了房间！')
            return
        self.is_room_owner = False
        self.can_start = True

        ip = text.get()
        if not isIP(ip):
            tk.messagebox.showinfo('错误', 'IP地址不合法或未输入！')
            return

        print(ip)
        self.tcp_control.set_ip(ip)
        thread_join = threading.Thread(target=self.tcp_control.join_room, args=(self.cond,))
        thread_join.daemon = True    # 设置为守护进程
        thread_join.start()

        exit_set = True
        while exit_set:
            temp_str = self.tcp_control.get_game_data()
            print(temp_str)
            if(temp_str != ''):
                if(temp_str[0:1] == '2'):
                    head, self.color, self.proi = temp_str.split('#')
                    if self.color == '0':
                        setcolor['text'] = '本方黑色'
                    else:
                        setcolor['text'] = '本方白色'
                        self.my_color = 'White'
                        self.other_color = 'Black'

                    if self.proi == '1':
                        setproi['text'] = '对方先手'
                        self.is_our_side = False
                    else:
                        setproi['text'] = '本方先手'
                        self.is_our_side = True

                    print(self.proi, self.color)
                    exit_set = False

        if self.proi == '1':    # 若房主先手，则需要将其消息监听进程切换到等待发送状态
            self.tcp_control.start(self.cond)
            callback_human = threading.Thread(target=self.other_human)
            callback_human.start()

    def setcolor(self, set):
        if not self.tcp_control.gameStart:
            if self.color == '1':
                set['text'] = '本方白色'
                self.color = '0'
                self.my_color = 'White'
                self.other_color = 'Black'
            else:
                set['text'] = '本方黑色'
                self.color = '1'

    def setproi(self, set):
        if not self.tcp_control.gameStart:
            if self.proi == '1':
                set['text'] = '对方先手'
                self.proi = '0'
                self.is_our_side = False
            else:
                set['text'] = '本方先手'
                self.proi = '1'
                self.is_our_side = True

    def render(self):
        self.update()

# 调试用
def main():
    view = CheckerBoardView()
    view.mainloop()

if __name__ == "__main__":
    main()