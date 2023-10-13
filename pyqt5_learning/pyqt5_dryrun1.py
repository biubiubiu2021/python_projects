# coding:utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Icon(QWidget):  # 继承了QWidget这个基类，并自定义了一个名为Icon的新类。同时对这个Icon的新类进行了初始化。

    def __init__(self):
        super().__init__()  # 要用QWidget中__init__的变量，就必须在子类Icon中显示调用：super().__init__()。__init __()方法是Python语言的初始化方法（构造函数）
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)  # 这个一下3个方法都是继承而来，这个方法=remove()+resize()
        self.setWindowTitle("hahaha")
        self.setWindowIcon(QIcon('1.ico'))  # 创建一个QIcon对象，QIcon接收到要显示的ico图标信息
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Icon()
    sys.exit(app.exec_())