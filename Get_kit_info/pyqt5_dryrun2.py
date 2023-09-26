# coding:utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton  # 引入QPushButton 类
from PyQt5.QtGui import QIcon  # 从PyQt5.QtGui中引入QIcon这个类，也是为了便于图标的设定。
from PyQt5.QtCore import QCoreApplication


class Icon(QWidget):  # 继承QWidget 这个基类， 并定义ICON新类
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("hahaha")
        self.setWindowIcon(QIcon('1.ico'))

        qbtn = QPushButton("Exit!", self)  # 创建一个QPushButton的实例，构造函数的第一个参数是按钮的标签，第二个参数是父窗口小部件，父窗口小部件是示例例窗口小部件，继承自QWidget
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(70, 30)
        qbtn.move(50, 50)
        #
        # PyQt5中的事件处理系统采用信号和槽机制构建。 如果我们点击按钮，点击的信号被发出。 槽可以是Qt槽函数或任何Python可调用的函数。 QCoreApplication包含主事件循环; 它处理和调度所有事件。 instance()方法给我们当前的实例。#
        # 请注意，QCoreApplication是通过QApplication创建的。 点击的信号连接到终止应用程序的quit()方法。
        # 通信在两个对象之间完成：发送方和接收方。 发送方是按钮，接收者是应用对象。
        # 简单的来说就是按钮发出被单击的信号，连接到退出程序的方法。

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Icon()
    sys.exit(app.exec_())
