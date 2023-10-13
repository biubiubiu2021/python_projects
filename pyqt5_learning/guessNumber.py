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
        self.bt1.setToolTip("<b>Click here to guess~</b>")#创建一个工具提示，我们调用setTooltip()方法。 我们可以使用富文本格式。鼠标停留在按钮上就会出现
        self.bt1.clicked.connect(self.showMessage)        #当按钮被单击时我们调用showMessage()方法去响应执行

        self.text = QLineEdit("Input a number here", self)#建立一个QLineEdit对象，用于让玩家输入数字。“在这里输入数字”是当窗口出现时出现的默认字符
        self.text.selectAll()#selectAll()方法则是可以理解为将“在这里输入数字”进行全选，方便输入数字，否则你还得手动全选删除默认字符
        self.text.setFocus()#selectAll()方法则是可以理解为将“在这里输入数字”进行全选，方便输入数字，否则你还得手动全选删除默认字符
        self.text.setGeometry(80,70,150,30)

        self.label = QLabel(self) #创建一个标签
        self.label.setText("猜一个1-100之间的整数") #标签内容
        self.label.setGeometry(20,20,250,30)
        self.label.setStyleSheet("QLabel{color:rgb(255,0,255,255);font-size:20px;font-weight:bold}") #设置标签格式

        self.show()

    def showMessage(self):#弹出一个对话框，告诉你结果是什么样的
        guess_number = int(self.text.text())#获取一个随机数
        print("\033[1;32;40m Guess again! \033[0m")

        if guess_number>self.num:
            QMessageBox.about(self, "Check the result", "Bigger then target!")
            self.text.setFocus()
            self.text.clear()#用户输完后清理窗口里的信息，方便下一次输入
        elif guess_number < self.num:
            QMessageBox.about(self, "Check the result", "Smaller then target!")
            self.text.clear()
        else:
            QMessageBox.about(self, "Check the result", "Right! you win! Next Round")
            self.num=randint(1,100)
            self.text.clear()
            self.text.setFocus()

    def closeEvent(self, event=None):#如果关闭QWidget，则生成QCloseEvent。 要修改widget的行为，需要重新实现closeEvent()事件处理程序。
        reply = QMessageBox.question(self,"Confirm", "Confirm quit?", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        #显示一个带有两个按钮的消息框：Yes和No。第一个字符串出现在标题栏上。 第二个字符串是对话框显示的消息文本。 第三个参数指定出现在对话框中的按钮的组合。
        #最后一个参数是默认按钮。 它是初始键盘焦点的按钮。 返回值存储在答复变量中。
        if reply == QMessageBox.Yes:
            event.accept()#接受导致关闭窗口小部件并终止应用程序的事件
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


