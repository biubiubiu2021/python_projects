import sys
from PyQt5.QtWidgets import QApplication,QMessageBox,QWidget,QPushButton,QHBoxLayout,QVBoxLayout
from random import randint

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("剪刀-石头-布")

        self.bt1 = QPushButton("剪刀",self)
        #self.bt1.setGeometry(30,180,50,50)
        self.bt2 = QPushButton("石头",self)
        #self.bt2.setGeometry(100,180,50,50)
        self.bt3 = QPushButton("布",self)
        #self.bt3.setGeometry(170,180,50,50)

        hbox = QHBoxLayout()#创建一个水平框布局,并添加一个拉伸因子和三个按钮。这个拉伸在三个按钮之前增加了一个可伸缩的空间。这将把它们推到窗口的右边。
        hbox.addStretch(1)#增加伸缩量
        hbox.addWidget(self.bt1)
        hbox.addStretch(1)#增加伸缩量
        hbox.addWidget(self.bt2)
        hbox.addStretch(1)#增加伸缩量
        hbox.addWidget(self.bt3)
        hbox.addStretch(6)#增加伸缩量
        #addStretch函数的作用是在布局器中增加一个伸缩量，里面的参数表示QSpacerItem的个数，默认值为零，会将你放在layout中的空间压缩成默认的大小。例如用addStretch函数实现将QHBoxLayout的布局器的空白空间分配。
        ##四个addStretch()函数用于在button按钮间增加伸缩量，伸缩量的比例为1:1:1:6，意思就是将button以外的空白地方按设定的比例等分为9份并按照设定的顺序放入布局器中。

        vbox = QVBoxLayout()#水平布局放置在垂直布局中。垂直框中的拉伸因子将按钮的水平框推到窗口的底部。
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)#设置窗口的主要布局
        self.show()


if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
