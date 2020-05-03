# -*- coding: utf-8 -*-
# 该文件用于进行联机时的网络通讯
# 文件名：tcp_server.py

# 导入 socket模块
import socket
import time


# 用于网络通讯的控制
class TCPConnect(object):
    # 定义公开属性
    recv_data = ''
    send_data = ''
    port = 1060    # 可修改为指定的端口通信
    flag = False    # 用于判断是否建立连接
    connect_ip = '127.0.0.1'
    gameStart = False

    # 返回本机IP地址，用于连接
    def get_my_ip(self):
        my_ip = socket.gethostbyname(socket.getfqdn(socket.gethostname()))  # 获取本机IP地址
        print(my_ip)  # 调试用
        return my_ip

    # 建立一个房间
    def create_room(self, cond):
        self.flag = True
        try:
            server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 建立socket，参数为ipv4，TCP，另一个参数默认为1.
            server_sock.bind(('127.0.0.1', self.port))  # self.port = 1060
            server_sock.listen(5)
            buffer = 1024
            print('服务器已经就绪......')
        except:
            self.flag = False
            print('服务器端建立连接错误，请检查端口和ip是否可用......')

        try:
            while True:
                # 循环接受客户端的连接请求
                connection, address = server_sock.accept()
                self.flag = True
                while True:
                    # 循环接收客户端发送的消息
                    client_msg = connection.recv(buffer)
                    print(client_msg)
                    if client_msg == '':
                        # 当接受到的clientMsg为空就跳出循环，出现过卡死状态
                        continue
                    elif client_msg == b'Y':
                        print('服务器端已经与客户端建立连接......')
                        connection.send('Y'.encode('utf-8'))
                        cond.acquire()
                        cond.notify()
                        cond.wait()  # 等待主进程通知发送数据
                        cond.release()
                        connection.send(self.send_data.encode('utf-8'))
                        print('!' + self.send_data)
                    elif client_msg == b'N':
                        print('服务器端与客户端建立连接失败......')
                        connection.send('N'.encode('utf-8'))
                    else:
                        self.recv_data = client_msg.decode()
                        cond.acquire()
                        cond.wait()    # 等待主进程通知发送下棋数据
                        connection.send(self.send_data.encode('utf-8'))
                        cond.release()
        except:
            print('连接错误......')

    def set_ip(self, ip):
        self.connect_ip = ip

    def join_room(self, cond):
        self.flag = True
        try:
            client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 建立socket，参数为ipv4，TCP，另一个参数默认为1.
            client_sock.connect((self.connect_ip, self.port))
            print('客户端已经就绪......')
            client_sock.send('Y'.encode('utf-8'))
        except:
            self.flag = False
            print('服务器端建立连接错误，请检查端口和ip是否可用......')
        while True:
            # 循环接收客户端发送的消息
            server_msg = client_sock.recv(1024)
            if server_msg == '':
                # 当接受到的clientMsg为空就跳出循环，出现过卡死状态
                continue
            elif server_msg == b'Y':
                self.gameStart = True
                print('客户端已经与服务器端建立连接......')
            elif server_msg == b'N':
                print('服务器端与客户端建立连接失败......')
            else:
                self.recv_data = server_msg.decode()
                cond.acquire()
                cond.wait()  # 等待主进程通知发送下棋数据
                cond.release()
                client_sock.send(self.send_data.encode('utf-8'))

    def send_pre_data(self, cond, color, is_priority):
        cond.acquire()
        cond.wait()
        self.send_data = '2' + '#' + color + '#' + is_priority
        cond.notify()
        cond.release()

    def send_game_data(self, cond, win, piece_num, x, y):
        cond.acquire()
        self.send_data = '3' + '#' + win + '#' + piece_num + '#' + x + '#' + y
        cond.notify()
        cond.release()

    def start(self, cond):
        cond.acquire()
        self.send_data = '4'
        cond.notify()
        cond.release()

    # 获得到数据的时间不确定（取决于对方的思考时间）
    def get_game_data(self):
        return_data = self.recv_data
        self.recv_data = ''    # 清空，避免重复获取
        return return_data

