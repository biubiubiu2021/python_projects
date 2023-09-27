import sys
from PyQt5.QtWidgets import QApplication,QMessageBox,QWidget,QPushButton
from random import randint

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("剪刀-石头-布")

        self.bt1 = QPushButton("剪刀",self)
        self.bt1.setGeometry(30,180,50,50)

        self.bt2 = QPushButton("石头",self)
        self.bt2.setGeometry(100,180,50,50)

        self.bt3 = QPushButton("布",self)
        self.bt3.setGeometry(170,180,50,50)

        self.bt1.clicked.connect(self.buttonclicked)#第一个窗口， 三个窗口都是信号发送者
        self.bt2.clicked.connect(self.buttonclicked)#三个按钮的clicked信号都连接到同一个槽buttonclicked
        self.bt3.clicked.connect(self.buttonclicked)
        #buttonClicked()方法中，我们通过调用sender()方法来确定点击了哪个按钮。



        self.show()



    def buttonclicked(self):
        computer = randint(1,3)
        player = 0
        sender = self.sender()#获取按钮，通过调用sender()方法来确定信号源
        print("--->",sender)
        print("--->",sender.text())#获取按钮的文本信息
        #---> <PyQt5.QtWidgets.QPushButton object at 0x0000025A66814D30>
        # ---> 剪刀
        # ---> <PyQt5.QtWidgets.QPushButton object at 0x0000025A66814DC0>
        # ---> 石头
        # ---> <PyQt5.QtWidgets.QPushButton object at 0x0000025A66814E50>
        # ---> 布

        if sender.text() =="剪刀":
            player =1
        elif sender.text() == "石头":
            player=2
        else:
            player=3

        if player == computer:
            QMessageBox.about(self,'结果', '平手！')
        elif player ==1 and computer==2:
            QMessageBox.about(self, '结果', '玩家： 剪刀， 电脑：石头！， ---> 电脑赢了！')
        elif player ==1 and computer==3:
            QMessageBox.about(self, '结果', '玩家： 剪刀， 电脑：布！， ---> 玩家赢了！')
        elif player == 2 and computer == 1:
            QMessageBox.about(self, '结果', '玩家： 石头， 电脑：剪刀！， ---> 玩家赢了！')
        elif player ==2 and computer==3:
            QMessageBox.about(self, '结果', '玩家： 石头， 电脑：布！， ---> 电脑赢了！')
        elif player ==3 and computer==1:
            QMessageBox.about(self, '结果', '玩家： 布， 电脑：剪刀！， ---> 电脑赢了！')
        elif player ==3 and computer==2:
            QMessageBox.about(self, '结果', '玩家： 布， 电脑：石头！， ---> 玩家赢了！')



if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
