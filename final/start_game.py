# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QDialog
from UI_game_begin import Ui_StartGame
from UI_select import Ui_select
from UI_develop import Ui_develop
import GUI_human
import GUI_human_vs_AI

# 开发日志
class develop(QDialog, Ui_develop):
    def __init__(self):
        super(develop, self).__init__()
        self.dialog = Ui_develop()
        self.setupUi(self)

# 难度选择
class ToSelect(QDialog, Ui_select):
    def __init__(self):
        super(ToSelect, self).__init__()
        self.select = Ui_select()
        self.setupUi(self)
        self.easy.clicked.connect(self.begin_easy)    # 绑定按钮事件
        self.normal.clicked.connect(self.begin_normal)
        self.hard.clicked.connect(self.begin_hard)

    def begin_easy(self):
        self.accept()    # 隐藏难度选择窗口
        while 1:
            view = GUI_human_vs_AI.CheckerBoardView(1)
            view.mainloop()
            if view.end:
                break

    def begin_normal(self):
        self.accept()
        while 1:
            view = GUI_human_vs_AI.CheckerBoardView(2)
            view.mainloop()
            if view.end:
                break

    def begin_hard(self):
        self.accept()
        while 1:
            view = GUI_human_vs_AI.CheckerBoardView(3)
            view.mainloop()
            if view.end:
                break

# 游戏进入界面
class MyMain(QDialog, Ui_StartGame):

    def __init__(self):
        super(MyMain, self).__init__()
        self.main = Ui_StartGame()
        self.setupUi(self)

        self.Human.clicked.connect(self.begin_human)
        
    # 启动局域网对战
    def begin_human(self):
        vs_human = GUI_human.CheckerBoardView()
        self.accept()
        vs_human.mainloop()

# 展示难度选择界面
def show_select(parent, child):
    parent.accept()
    child.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 实例化
    begin = MyMain()
    child = ToSelect()
    dialog = develop()
    # 事件绑定
    begin.AI.clicked.connect(lambda: show_select(begin, child))
    begin.develop.clicked.connect(dialog.show)

    begin.show()
    sys.exit(app.exec_())