from PyQt5.QtWidgets import QWidget,QCheckBox,QApplication,QPushButton,QMessageBox
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("hahaha")
        self.setGeometry(600,300,200,300)

        #新建4个复选框对象
        self.checkBox1 = QCheckBox("select all",self)
        self.checkBox2 = QCheckBox("option1", self)
        self.checkBox3 = QCheckBox("option2", self)
        self.checkBox4 = QCheckBox("option3", self)
        self.button1 = QPushButton("Submit", self)

        self.checkBox1.move(20,20)
        self.checkBox2.move(40, 60)
        self.checkBox3.move(40, 100)
        self.checkBox4.move(40, 140)
        self.button1.move(60,180)

        #每当复选框的状态改变时，即每当用户选中或取消选中该信号时，就会发出此信号。
        # 所以当产生此信号的时候，我们将其连接相应的槽函数。其中全选（cb1）那个复选框对应的是changecb1，其它的是changecb2。
        self.checkBox1.stateChanged.connect(self.change_check_box1)
        self.checkBox2.stateChanged.connect(self.change_check_box2)
        self.checkBox3.stateChanged.connect(self.change_check_box2)
        self.checkBox4.stateChanged.connect(self.change_check_box2)
        self.button1.clicked.connect(self.go)

        self.show()


    def change_check_box1(self):#cb1如果被选中，那么cb2、cb3、cb4也将被选中，实现全选功能。要是没有被选中，那么cb2、cb3、cb4也将没有被选中，实现反选功能。
        print("is checked")
        print("0------->", self.checkBox1.checkState())
        if self.checkBox1.checkState() == Qt.Checked:
            print("All options are checked!")
            self.checkBox2.setChecked(True)
            self.checkBox3.setChecked(True)
            self.checkBox4.setChecked(True)
        elif self.checkBox1.checkState() == Qt.Unchecked:
            print("All options are NOT checked!")
            self.checkBox2.setChecked(False)
            self.checkBox3.setChecked(False)
            self.checkBox4.setChecked(False)
    def change_check_box2(self):
        if self.checkBox2.isChecked() and self.checkBox3.isChecked() and self.checkBox4.isChecked():#isChecked()主要是判断复选框是否被选中，要是选中就返回True，否则返回False
            self.checkBox1.setCheckState(Qt.Checked)#如果cb2、cb3、cb4都被选中，那么cb1（全选）就会被选中
        elif self.checkBox2.isChecked() or self.checkBox3.isChecked() or self.checkBox4.isChecked():
            self.checkBox1.setTristate()#如果cb2、cb3、cb4有一个被选中，那么cb1（全选）就会被半选
            self.checkBox1.setCheckState(Qt.PartiallyChecked)
        else:#cb2、cb3、cb4没有一个被选中，那么cb1（全选）就不会被选中。
            self.checkBox1.setTristate(False)
            self.checkBox1.setCheckState(Qt.Unchecked)


    def go(self):
        if self.checkBox2.isChecked() and self.checkBox3.isChecked() and self.checkBox4.isChecked():
            QMessageBox.information(self,"select all 1,2,3","1/2/3")
        elif self.checkBox2.isChecked() and self.checkBox3.isChecked():
            QMessageBox.information(self,"select 1,2","1/2")
        elif self.checkBox2.isChecked() and self.checkBox4.isChecked():
            QMessageBox.information(self,"select 1,3","1/3")
        elif self.checkBox3.isChecked() and self.checkBox4.isChecked():
            QMessageBox.information(self,"select 2,3","2/3")
        elif self.checkBox2.isChecked():
            QMessageBox.information(self, "select 1", "1")
        elif self.checkBox3.isChecked():
            QMessageBox.information(self, "select 2", "2")
        elif self.checkBox4.isChecked():
            QMessageBox.information(self, "select 3", "3")
        else:
            QMessageBox.information(self, "No select ", "0")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())