# coding:utf-8
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QMessageBox,QLineEdit,QLabel
from PyQt5.QtGui import QIcon
from random import randint

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.num = randint(1,100)#类在进行初始化的时候，自动产生一个1-100的随机整数。

    def initUI(self):
        self.setGeometry(300,300,300,220)
        self.setWindowTitle("Guess the Number")
        self.setWindowIcon(QIcon("1.ico"))

        self.bt1 = QPushButton("Guess", self)
        self.bt1.setGeometry(115,150,70,30)
        self.bt1.setToolTip("<b>Click here to guess~</b>")
        self.bt1.clicked.connect(self.showMessage)

        self.text = QLineEdit("Input a number here", self)
        self.text.selectAll()
        self.text.setFocus()
        self.text.setGeometry(80,70,150,30)

        self.label = QLabel(self)
        self.label.setText("猜一个1-100之间的整数")
        self.label.setGeometry(20,20,250,30)
        self.label.setStyleSheet("QLabel{color:rgb(255,0,255,255);font-size:20px;font-weight:bold}")
        self.show()

    def showMessage(self):
        guess_number = int(self.text.text())
        print("\033[1;32;40m Guess again! \033[0m")

        if guess_number>self.num:
            QMessageBox.about(self, "Check the result", "Bigger then target!")
            self.text.setFocus()
            self.text.clear()
        elif guess_number < self.num:
            QMessageBox.about(self, "Check the result", "Smaller then target!")
            self.text.clear()
        else:
            QMessageBox.about(self, "Check the result", "Right! you win! Next Round")
            self.num=randint(1,100)
            self.text.clear()
            self.text.setFocus()

    def closeEvent(self, event=None):
        reply = QMessageBox.question(self,"Confirm", "Confirm quit?", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


