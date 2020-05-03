# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_develop.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_develop(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 530)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(225, 10, 250, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(0, 70, 700, 461))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "开发日志"))
        self.label.setText(_translate("Dialog", "开   发   日   志"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">2019年6月26日 Ver1.0.0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-weight:400;\">l</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400;\">  </span><span style=\" font-weight:400;\">完成了判断胜负，落子等基础功能，使用Tkinter完成了基础图形界面，现在可以在一台电脑上通过鼠标点击实现自己和自己对战了。 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">2019年6月27日 Ver1.1.0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-weight:400;\">l</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400;\">  </span><span style=\" font-weight:400;\">解决了边角棋子显示不完全的BUG </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-weight:400;\">l</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400;\">  </span><span style=\" font-weight:400;\">添加了开始游戏按钮，修改了图形界面响应逻辑 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">2019年6月29日 Ver1.2.0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-weight:400;\">l</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400;\">  </span><span style=\" font-weight:400;\">使用Q-learning写了第一版五子棋AI，效果不佳 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-weight:400;\">l</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400;\">  </span><span style=\" font-weight:400;\">改变了棋盘界面颜色，现在界面更加清爽了 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2019年6月30日 Ver1.4.0<span style=\" font-weight:400;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-weight:400;\">l</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400;\">  </span><span style=\" font-weight:400;\">改变了五子棋AI的算法，使用alpha-beta剪枝博弈树搜索算法完成第二版五子棋AI。 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-weight:400;\">l</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400;\">  </span><span style=\" font-weight:400;\">已知BUG：1、玩家对相同位置重复落子被判定为有效 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">2、由于程序使用单线程，AI在计算落子位置时界面会未响应 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">2019年7月1日 Ver1.5.0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">解决了重复落子判定问题，优化了五子棋AI在部分棋型情况下的计算速度。 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2019年7月2日 Ver1.6.0<span style=\" font-weight:400;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-weight:400;\">l</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400;\">  </span><span style=\" font-weight:400;\">增加了局域网对战功能，玩家可以选择建立房间和加入房间，房主默认为黑色棋子且先手 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-weight:400;\">l</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400;\">  </span><span style=\" font-weight:400;\">已知BUG：由于程序是单线程的，所以在对方回合时会造成棋盘未响应，回到我方回合时即恢复正常 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">2019年7月3日 Ver1.7.0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-weight:400;\">l</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400;\">  </span><span style=\" font-weight:400;\">修复了双人对战功能无法正常进行胜负判定功能的BUG </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-weight:400;\">l</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400;\">  </span><span style=\" font-weight:400;\">修复了双人对战功能没有开始游戏就能下子的BUG </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">2019年7月4日 Ver1.8.0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-weight:400;\">l</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400;\">  </span><span style=\" font-weight:400;\">双人对战功能现在可以由房主选择黑/白方和先/后手了，另一方将随房主设置自动应用 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2019年7月5日 Ver2.0.0 </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-weight:400;\">l</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400;\">  </span><span style=\" font-weight:400;\">使用pyQT制作了初始界面和功能选择（人机/人人）界面，现在游戏的可交互性更强了 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-weight:400;\">l</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400;\">  </span><span style=\" font-weight:400;\">现在人机AI根据搜索深度被分为简单，一般，困难三个难度级别了，可以自由选择挑战 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-weight:400;\">l</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400;\">  </span><span style=\" font-weight:400;\">已知问题：困难级别AI的计算时间过长，仍然需要优化，在10步棋之后的响应时间达到了2分钟 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">2019年7月6日 Ver2.1.0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-weight:400;\">l</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400;\">  </span><span style=\" font-weight:400;\">为人机对战模式增加了悔棋、禁手（详细规则见后）、重新开始、退出游戏等功能按钮 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-weight:400;\">l</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400;\">  </span><span style=\" font-weight:400;\">为人和不同难度的AI制作了不同的头像，按钮制作为配套风格 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">2019年7月7日 Ver2.2.0 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-weight:400;\">l</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400;\">  </span><span style=\" font-weight:400;\">在人机对战模式中增加了哪方下子的提示信息 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-weight:400;\">l</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400;\">  </span><span style=\" font-weight:400;\">增加了落子信息提示框，妈妈再也不用担心我找不到上一步落子位置了！ </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Wingdings\'; font-weight:400;\">l</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-weight:400;\">  </span><span style=\" font-weight:400;\">由于局域网对战模式涉及到数据传递问题较难解决，目前增加的功能性按钮均只应用于人机模式 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">  </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'微软雅黑,sans-serif\'; color:#000000;\">附1 禁手规则：该规则开启后对黑方有效</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'微软雅黑,sans-serif\'; font-weight:400; color:#000000;\">1．三、三禁手</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'微软雅黑,sans-serif\'; font-weight:400; color:#000000;\">黑方一子落下同时形成两个或两个以上的活三（或嵌四），此步为三三禁手。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'微软雅黑,sans-serif\'; font-weight:400; color:#000000;\">2．四、四禁手</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'微软雅黑,sans-serif\'; font-weight:400; color:#000000;\">黑方一子落下同时形成两个或两个以上的四，活四、冲四、嵌五之四，包括在此四之内。此步为四四禁手。注意：只要是两个“四”即为禁手，无论是哪种四，活四，跳四，冲四都算。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'微软雅黑,sans-serif\'; font-weight:400; color:#000000;\">3．四、三、三禁手</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'微软雅黑,sans-serif\'; font-weight:400; color:#000000;\">黑方一步使一个四，两个活三同时形成。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'微软雅黑,sans-serif\'; font-weight:400; color:#000000;\">4．四、四、三禁手</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'微软雅黑,sans-serif\'; font-weight:400; color:#000000;\">黑方一步使两个四，一个活三同时形成。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'微软雅黑,sans-serif\'; font-weight:400; color:#000000;\">5．长连禁手</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'微软雅黑,sans-serif\'; font-weight:400; color:#000000;\">黑方一子落下形成连续六子或六子以上相连</span><span style=\" font-family:\'Courier New\'; font-weight:400;\"> </span></p></body></html>"))

