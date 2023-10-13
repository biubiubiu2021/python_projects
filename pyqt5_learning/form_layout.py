import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QFormLayout,QLabel,QLineEdit,QTextEdit

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("Forms")

        formlayout = QFormLayout() #创建一个表单布局
        nameLabel = QLabel("姓名")
        nameLineEdit = QLineEdit("")
        introductionLabel = QLabel("简介")
        introductionLineEdit = QTextEdit("")

        formlayout.addRow(nameLabel,nameLineEdit)    #向表单中增加一行，内容是我们定义的小部件。
        formlayout.addRow(introductionLabel,introductionLineEdit)

        self.setLayout(formlayout)

        self.show()

if __name__ =="__main__":
    app=QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())