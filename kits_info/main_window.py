from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QInputDialog,QTextBrowser,QTextEdit,QCheckBox, QTableWidget,QTableWidgetItem
import sys
from get_all_kits_name import get_all_kits_name
from Get_kits_detail_single_kit_DICT import get_single_kit_info
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from Get_kits_detail_compare_2kits_clean import getKitDetails
import subprocess
import shlex
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



        self.checkBox1 = QCheckBox("CentOS",self)
        self.checkBox2 = QCheckBox("Windows", self)
        self.checkBox3 = QCheckBox("ESXi", self)
        self.checkBox4 = QCheckBox("Redhat", self)


        # self.checkBox1.move(300, 390)
        # self.checkBox2.move(300, 410)
        # self.checkBox3.move(300, 430)
        # self.checkBox4.move(300, 450)
        self.label3 = QLabel("Select an OS:", self)
        self.label3.resize(65,12)
        self.label3.move(20, 20)

        self.checkBox1.move(100, 20)
        self.checkBox2.move(170, 20)
        self.checkBox3.move(240, 20)
        self.checkBox4.move(310, 20)

        self.checkBox1.stateChanged.connect(self.get_check_box_status1)
        self.checkBox2.stateChanged.connect(self.get_check_box_status2)
        self.checkBox3.stateChanged.connect(self.get_check_box_status3)
        self.checkBox4.stateChanged.connect(self.get_check_box_status4)

        self.bt1 = QPushButton("Select a Kit:", self)
        #self.bt1.resize(65,20)
        self.bt1.move(390, 15)

        self.bt1.clicked.connect(self.show_dialog)



        self.text = QTextEdit(self)
        self.text.setGeometry(20,80,100,270)
        self.text5 = QTextEdit(self)
        self.text5.setGeometry(120,80,400,270)

        self.text2 = QTextEdit("NA", self)
        self.text2.setGeometry(20, 390,200,100)

        self.label4 = QLabel("Compare 2 kit:",self)
        self.label4.resize(70,12)
        self.label4.move(230, 370)

        self.text3 = QTextEdit(self)
        self.text3.setGeometry(230,390,210,20)
        self.text4 = QTextEdit(self)
        self.text4.setGeometry(230, 420, 210, 20)

        self.bt2 = QPushButton("Select Kit1", self)
        #self.bt1.resize(105,20)
        self.bt2.move(420, 390)
        self.bt3 = QPushButton("Select Kit2", self)
        #self.bt1.resize(65,20)
        self.bt3.move(420, 420)

        self.bt2.clicked.connect(self.get_kit1)
        self.bt3.clicked.connect(self.get_kit2)

        self.bt4 = QPushButton("Compare", self)
        self.bt4.move(390,460)
        self.bt4.clicked.connect(self.compare_2_kits)




        self.show()


    def show_dialog(self):
        text = ""
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
            print(kitDetail.keys())
            #self.text.append(text)
            self.text.setCurrentFont(QFont("Arial",8))
            for item in kitDetail.keys():
                print("--->",item)
                self.text.append(item)
            for item in kitDetail.values():
                print("--->",item)
                item = "VERSION: " + item
                self.text5.append(item)
        #return text

    def get_kit1(self):
        text = ""
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
        if sender == self.bt2:

            text, ok = QInputDialog.getItem(self,"Select kits", "Pls Select a kit:", kits)
            # 可以输入选择项，待选放到列表中，这里的列表就是sex
            if ok:
                self.text3.clear()

            #kitDetail = get_single_kit_info(text)
            self.text3.append(text)
            self.text3.setCurrentFont(QFont("Arial",8))

    def get_kit2(self):
        text = ""
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
        if sender == self.bt3:

            text, ok = QInputDialog.getItem(self,"Select kits", "Pls Select a kit:", kits)
            # 可以输入选择项，待选放到列表中，这里的列表就是sex
            if ok:
                self.text4.clear()

            #kitDetail = get_single_kit_info(text)
            self.text4.append(text)
            self.text4.setCurrentFont(QFont("Arial",8))

    def compare_2_kits(self):
        print_list=[]
        print("------------compare")
        kitID1 = self.text3.toPlainText()
        print("************>", kitID1)
        kitID2 = self.text4.toPlainText()
        print("************>", kitID2)
        # kitDict1 = get_single_kit_info(kitID1)
        # kitDict2 = get_single_kit_info(kitID2)
        kitDict1 = getKitDetails(kitID1)
        kitDict2 = getKitDetails(kitID2)

        print(kitDict1)
        print(kitDict2)
        print(f"\033[1;32mKit Name(Candidate): %-*s |%-*s\033[0m" % (82, kitID1, 1, ""), "\033[1;33mKit Name(Newer): %-*s |%-*s\033[0m" % (91, kitID2, 1, ""))
        for key in kitDict1.keys():
            if kitDict1[key] == kitDict2[key]:
                print("ingredient: %-*s Version: %-*s  |%-*s" % (20, key, 60, kitDict1[key], 1, ""),"ingredient: %-*s Version: %-*s  |%-*s" % (20, key, 65, kitDict2[key], 20, ""))
            else:
                print("ingredient: %-*s Version: \033[0;31m%-*s\033[0m  |%-*s" % (20, key, 62, kitDict1[key], 1, ""), "ingredient: %-*s Version: \033[0;31m%-*s\033[0m  |%-*s" % (20, key, 62, kitDict2[key], 20, ""))

        #########################

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