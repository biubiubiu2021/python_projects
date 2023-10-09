from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QCheckBox
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,330,300)
        self.setWindowTitle("haha")

        self.label = QLabel("display the single info",self)
        self.label.setFixedWidth(200)
        self.label.move(20,20)
        self.bt1 = QPushButton('提示',self)
        self.bt1.move(20,70)
        self.bt2 = QPushButton('询问',self)
        self.bt2.move(120,70)
        self.bt3 = QPushButton('警告',self)
        self.bt3.move(220,70)
        self.bt4 = QPushButton('错误',self)
        self.bt4.move(20,140)
        self.bt5 = QPushButton('关于',self)
        self.bt5.move(120,140)
        self.bt6 = QPushButton('关于Qt',self)
        self.bt6.move(220,140)

        self.bt1.clicked.connect(self.info)
        self.bt2.clicked.connect(self.question)
        self.bt3.clicked.connect(self.warning)
        self.bt4.clicked.connect(self.critical)
        self.bt5.clicked.connect(self.about)

        self.show()

    def info(self):
        reply = QMessageBox.information(self,"note:", "This is a Note dialog", QMessageBox.Ok| QMessageBox.Close, QMessageBox.Close)
        if reply == QMessageBox.Ok:
            self.label.setText("You select OK!")
        else:
            self.label.setText("You select Close!")

    def question(self):
        reply = QMessageBox.question(self,"question:","This is a question dialog, default answer is NO", QMessageBox.Yes | QMessageBox.No |QMessageBox.Cancel, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.label.setText("You choose Yes!")
        elif reply == QMessageBox.No:
            self.label.setText("You choose No!")
        elif reply == QMessageBox.Cancel:
            self.label.setText("You choose Cancel!")

    def warning(self):
        #reply = QMessageBox.warning(self,"Warning", "This is a warning message dialog", QMessageBox.Save|QMessageBox.Discard|QMessageBox.Cancel, QMessageBox.Save)
        cb = QCheckBox("do for all docs")
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Warning!")
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("This is a warning dialog")
        msgBox.setInformativeText("save the changes?")
        Save = msgBox.addButton("Save", QMessageBox.AcceptRole)
        NoSave = msgBox.addButton("Cancel", QMessageBox.ResetRole)
        Cancel = msgBox.addButton("Discard", QMessageBox.DestructiveRole)
        msgBox.setDefaultButton(Save)
        msgBox.setCheckBox(cb)
        cb.stateChanged.connect(self.check)
        reply = msgBox.exec()
        if reply == QMessageBox.AcceptRole:
            self.label.setText("you choose to save!")
        elif reply == QMessageBox.ResetRole:
            self.label.setText("you choose to Cancel!")
        else:
            self.label.setText("You choose to discard!")

    def check(self):
        if self.sender().isChecked():
            self.label.setText("double check you choose Yes")
        else:
            self.label.setText("double check you choose NO")

    def critical(self):
        #reply = QMessageBox.critical(self, "Error", "This is a Error dialog", QMessageBox.Retry|QMessageBox.Abort|QMessageBox.Ignore, QMessageBox.Retry)
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Warning!")
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("This is a error info dialog")
        msgBox.setStandardButtons(QMessageBox.Retry| QMessageBox.Abort |QMessageBox.Ignore)
        msgBox.setDefaultButton(QMessageBox.Retry)
        msgBox.setDetailedText("this is the detail info")
        reply = msgBox.exec()
        if reply == QMessageBox.Retry:
            self.label.setText("you choose to retry!")
        elif reply == QMessageBox.Abort:
            self.label.setText("you choose to Abort!")
        else:
            self.label.setText("You choose to ignore!")

    def about(self):
        QMessageBox.about(self,"about", "this is a message dialog")
        msgBox = QMessageBox(QMessageBox.NoIcon,"about", "66666666")
        msgBox.setIconPixmap(QPixmap("./1.ico"))
        msgBox.exec()



if __name__ =="__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())