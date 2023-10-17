from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QInputDialog, QTextBrowser, QTextEdit, QCheckBox, QTableWidget, QTableWidgetItem, QHBoxLayout, QDialog
from PyQt5.QtGui import QColor
import sys
from PyQt5 import QtCore
from get_all_kits_name import get_all_kits_name
from Get_kits_detail_single_kit_DICT import get_single_kit_info,getKitDetails
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import subprocess
import shlex

class TableWindow(QDialog):
    def __init__(self, data1, data2, ID1, ID2):
        super().__init__()
        self.setWindowTitle(f"Compare 2 kits:                       [{ID1}] ------------------------ VS ------------------------- {ID2}")
        self.setFixedSize(1000,400)
        self.table1 = QTableWidget()
        self.table1.setRowCount(len(data1))
        self.table1.setColumnCount(2)
        self.table1.setHorizontalHeaderLabels(["Ingredient", "Version"])

        for row, (ingredient, version) in enumerate(data1.items()):
            item_ingredient = QTableWidgetItem(ingredient)
            item_version = QTableWidgetItem(version)
            self.table1.setItem(row, 0, item_ingredient)
            self.table1.setItem(row, 1, item_version)
        self.table1.resizeColumnsToContents()
        self.table1.resizeRowsToContents()

        self.table2 = QTableWidget()
        self.table2.setRowCount(len(data2))
        self.table2.setColumnCount(2)
        self.table2.setHorizontalHeaderLabels(["Ingredient", "Version"])

        for row, (ingredient, version) in enumerate(data2.items()):
            item_ingredient = QTableWidgetItem(ingredient)
            item_version = QTableWidgetItem(version)
            self.table2.setItem(row, 0, item_ingredient)
            self.table2.setItem(row, 1, item_version)
        self.table2.resizeColumnsToContents()
        self.table2.resizeRowsToContents()

        self.compareTables()

        layout = QHBoxLayout()
        layout.addWidget(self.table1)
        layout.addWidget(self.table2)
        self.setLayout(layout)

    def compareTables(self):
        for row in range(self.table1.rowCount()):
            ingredient1 = self.table1.item(row, 0).text()
            version1 = self.table1.item(row, 1).text()

            ingredient2 = self.table2.item(row, 0).text()
            version2 = self.table2.item(row, 1).text()

            if ingredient1 == ingredient2 and version1 != version2:
                self.table1.item(row, 1).setBackground(QColor("red"))
                self.table2.item(row, 1).setBackground(QColor("red"))



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.OS = "CENTOS"

    def initUI(self):
        self.setGeometry(500,500,510,600)
        self.setWindowTitle("Check kit ingredients")

        self.table = QTableWidget(self)
        self.table.setGeometry(20, 80, 500, 370)
        # Set the table headers

        self.table.setRowCount(15)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Ingredient", "Version"])
        self.table.setColumnWidth(0, 100)
        self.table.setColumnWidth(1, 500)
        for i in range(0,15):
            self.table.setRowHeight(i, 5)


        self.label1 = QLabel("Kit Name:", self)
        self.label1.move(20,50)

        self.label2 = QLabel("NA", self)
        self.label2.resize(200,12)
        self.label2.move(80, 50)

        self.label3 = QLabel("Newest 5 Kits Name:", self)
        self.label3.resize(200,12)
        self.label3.move(20, 470)



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



        #self.text = QTextEdit(self)
        #self.text.setGeometry(20,80,100,270)
        #self.text5 = QTextEdit(self)
        #self.text5.setGeometry(120,80,400,270)

        self.text2 = QTextEdit("NA", self)
        self.text2.setGeometry(20, 490,200,100)

        self.label4 = QLabel("Compare 2 kit:",self)
        self.label4.resize(70,12)
        self.label4.move(230, 470)

        self.text3 = QTextEdit(self)
        self.text3.setGeometry(230,490,210,20)
        self.text4 = QTextEdit(self)
        self.text4.setGeometry(230, 520, 210, 20)

        self.bt2 = QPushButton("Select Kit1", self)
        #self.bt1.resize(105,20)
        self.bt2.move(430, 488)
        self.bt3 = QPushButton("Select Kit2", self)
        #self.bt1.resize(65,20)
        self.bt3.move(430, 518)

        self.bt2.clicked.connect(self.get_kit1)
        self.bt3.clicked.connect(self.get_kit2)

        # self.bt4 = QPushButton("Compare", self)
        # self.bt4.move(390,560)
        # self.bt4.clicked.connect(self.compare_2_kits)

        self.button = QPushButton("Compare2", self)
        self.button.move(390,560)
        self.button.clicked.connect(self.compare_2kits)



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
            # 可以输入选择项，待选放到列表中，这里的列表就是kits
            if ok:
                self.label2.setText(text)
                #self.text.clear()
            else:
                self.label2.clear()

            kitDetail = get_single_kit_info(text)
            print("-=-=-=->",kitDetail)
        for row, (ingredient, version) in enumerate(kitDetail.items()):
            item_ingredient = QTableWidgetItem(ingredient)
            item_version = QTableWidgetItem(version)
            self.table.setItem(row, 0, item_ingredient)
            self.table.setItem(row, 1, item_version)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

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
    def compare_2kits(self):
        print_list=[]
        print("------------compare")
        kitID1 = self.text3.toPlainText()
        print("************>", kitID1)
        kitID2 = self.text4.toPlainText()
        print("************>", kitID2)
        kitDict1 = get_single_kit_info(kitID1)
        kitDict2 = get_single_kit_info(kitID2)
        #kitDict1 = getKitDetails(kitID1)
        #kitDict2 = getKitDetails(kitID2)
        print("kit1--->", kitDict1)
        print("kit2--->", kitDict2)

        window = TableWindow(kitDict1, kitDict2, kitID1, kitID2)
        window.exec_()

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
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app=QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())