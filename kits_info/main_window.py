from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QInputDialog,QTextBrowser,QTextEdit,QCheckBox
import sys
from get_all_kits_name import get_all_kits_name
from Get_kits_detail_single_kit import get_single_kit_info
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.OS = "CENTOS"

    def initUI(self):
        self.setGeometry(2800,500,500,500)
        self.setWindowTitle("Check kit ingredients")

        self.label1 = QLabel("Kit Name:", self)
        self.label1.move(20,40)

        self.label2 = QLabel("NA", self)
        self.label2.resize(200,12)
        self.label2.move(80, 40)

        self.label3 = QLabel("Newest 5 Kits Name:", self)
        self.label3.resize(200,12)
        self.label3.move(20, 370)

        self.label3 = QLabel("Select an OS:", self)
        self.label3.resize(200,12)
        self.label3.move(280, 370)

        self.checkBox1 = QCheckBox("CentOS",self)
        self.checkBox2 = QCheckBox("Windows", self)
        self.checkBox3 = QCheckBox("ESXi", self)
        self.checkBox4 = QCheckBox("Redhat", self)


        self.checkBox1.move(300, 390)
        self.checkBox2.move(300, 410)
        self.checkBox3.move(300, 430)
        self.checkBox4.move(300, 450)

        self.checkBox1.stateChanged.connect(self.get_check_box_status1)
        self.checkBox2.stateChanged.connect(self.get_check_box_status2)
        self.checkBox3.stateChanged.connect(self.get_check_box_status3)
        self.checkBox4.stateChanged.connect(self.get_check_box_status4)





        self.text = QTextEdit(self)
        self.text.setGeometry(20,80,450,270)

        self.text2 = QTextEdit("NA", self)
        self.text2.setGeometry(20, 390,200,100)

        self.bt1 = QPushButton("Select a Kit:", self)
        self.bt1.move(390, 440)

        self.bt1.clicked.connect(self.show_dialog)

        self.show()

    def show_dialog(self):
        print("1---->", self.OS)
        sender = self.sender()
        kits= ["BHS-GNR-AP-CENTOS-23.41.5.81"]
        if self.OS == "CENTOS":
            kits = get_all_kits_name("CentOS")
        elif self.OS == "WIN":
            kits = get_all_kits_name("WIN")
        elif self.OS == "ESXI":
            kits = get_all_kits_name("ESXI")
        else:
            kits = get_all_kits_name("RHEL")

        print(kits)
        kits.reverse()
        print(kits)
        print("---->",sender)
        self.text2.clear()
        for i in range(0,5):
            self.text2.append(kits[i])

        if sender == self.bt1:

            text, ok = QInputDialog.getItem(self,"Select kits", "Pls Select a kit:", kits)
            # 可以输入选择项，待选放到列表中，这里的列表就是sex
            if ok:
                self.label2.setText(text)
                self.text.clear()

            kitDetail = get_single_kit_info(text)
            print(kitDetail)
            self.text.append(text)
            self.text.setCurrentFont(QFont("Arial",8))
            for item in kitDetail:
                print("--->",item)
                self.text.append(item)



    def get_check_box_status1(self):
        if self.checkBox1.checkState() == Qt.Checked:
            print("User select CentOS")
            self.OS = "CENTOS"
            self.checkBox2.setChecked(False)
            self.checkBox3.setChecked(False)
            self.checkBox4.setChecked(False)

    def get_check_box_status2(self):
        if self.checkBox2.checkState() == Qt.Checked:
            print("User select Windows")
            self.OS = "WIN"
            self.checkBox1.setChecked(False)
            self.checkBox3.setChecked(False)
            self.checkBox4.setChecked(False)

    def get_check_box_status3(self):
        if self.checkBox3.checkState() == Qt.Checked:
            print("User select Esxi")
            self.OS = "ESXI"
            self.checkBox1.setChecked(False)
            self.checkBox2.setChecked(False)
            self.checkBox4.setChecked(False)

    def get_check_box_status4(self):
        if self.checkBox4.checkState() == Qt.Checked:
            print("User select RHEL")
            self.OS = "RHEL"
            self.checkBox1.setChecked(False)
            self.checkBox2.setChecked(False)
            self.checkBox3.setChecked(False)


if __name__ =='__main__':
    app=QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())