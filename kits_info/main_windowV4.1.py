from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QInputDialog,QVBoxLayout,QMessageBox, QTextBrowser, QTextEdit, QCheckBox, QTableWidget, QTableWidgetItem, QHBoxLayout, QDialog
from PyQt5.QtGui import QColor
import sys
from PyQt5 import QtCore
from Get_kits_detail_single_kit_DICT import get_single_kit_info,getKitDetails,get_all_kits_name
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from urllib.request import urlopen
from urllib.request import urlopen
from urllib.error import URLError
import requests
import subprocess
import shlex
def url_exists(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException as err:
        print(f"URL doesn't exist: {url}")
        return False

class TableWindow(QDialog):
    def __init__(self, data1, data2, ID1, ID2):
        super().__init__()
        self.setWindowTitle(f"Compare 2 kits:                       [{ID1}] ------------------------ VS ------------------------- [{ID2}]")
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

class TableWindow2(QDialog):
    def __init__(self, data1, data2, data3, data4, data5):
        super().__init__()
        self.setWindowTitle(f"show 5 kits")
        self.setFixedSize(1600, 420)
        #Table1
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
        #Table2
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


        self.table3 = QTableWidget()
        self.table3.setRowCount(len(data3))
        self.table3.setColumnCount(2)
        self.table3.setHorizontalHeaderLabels(["Ingredient", "Version"])

        for row, (ingredient, version) in enumerate(data3.items()):
            item_ingredient = QTableWidgetItem(ingredient)
            item_version = QTableWidgetItem(version)
            self.table3.setItem(row, 0, item_ingredient)
            self.table3.setItem(row, 1, item_version)
        self.table3.resizeColumnsToContents()
        self.table3.resizeRowsToContents()

        #Table4
        self.table4 = QTableWidget()
        self.table4.setRowCount(len(data4))
        self.table4.setColumnCount(2)
        self.table4.setHorizontalHeaderLabels(["Ingredient", "Version"])

        for row, (ingredient, version) in enumerate(data4.items()):
            item_ingredient = QTableWidgetItem(ingredient)
            item_version = QTableWidgetItem(version)
            self.table4.setItem(row, 0, item_ingredient)
            self.table4.setItem(row, 1, item_version)
        self.table4.resizeColumnsToContents()
        self.table4.resizeRowsToContents()

        #Table5
        self.table5 = QTableWidget()
        self.table5.setRowCount(len(data5))
        self.table5.setColumnCount(2)
        self.table5.setHorizontalHeaderLabels(["Ingredient", "Version"])

        for row, (ingredient, version) in enumerate(data5.items()):
            item_ingredient = QTableWidgetItem(ingredient)
            item_version = QTableWidgetItem(version)
            self.table5.setItem(row, 0, item_ingredient)
            self.table5.setItem(row, 1, item_version)
        self.table5.resizeColumnsToContents()
        self.table5.resizeRowsToContents()

        self.compareTables2()

        layout = QHBoxLayout()
        layout.addWidget(self.table1)
        layout.addWidget(self.table2)
        layout.addWidget(self.table3)
        layout.addWidget(self.table4)
        layout.addWidget(self.table5)
        self.setLayout(layout)

    def compareTables3(self):
        for row in range(self.table1.rowCount()):
            ingredient1 = self.table1.item(row, 0).text()
            version1 = self.table1.item(row, 1).text()

            ingredient2 = self.table2.item(row, 0).text()
            version2 = self.table2.item(row, 1).text()

            ingredient3 = self.table3.item(row, 0).text()
            version3 = self.table3.item(row, 1).text()

            ingredient4 = self.table4.item(row, 0).text()
            version4 = self.table4.item(row, 1).text()

            ingredient5 = self.table5.item(row, 0).text()
            version5 = self.table5.item(row, 1).text()

            if row == 0:  # This is the first row
                color = QColor("green")  # Change this to whatever color you want
            else:
                color = QColor("red")

            if ingredient1 == ingredient2 == ingredient3 == ingredient4 == ingredient5 and \
                    (version1 != version2 or version1 != version3 or version1 != version4 or version1 != version5):
                self.table1.item(row, 1).setForeground(color)
                self.table2.item(row, 1).setForeground(color)
                self.table3.item(row, 1).setForeground(color)
                self.table4.item(row, 1).setForeground(color)
                self.table5.item(row, 1).setForeground(color)

    def compareTables2(self):
        colors = ["red", "blue", "brown", "Cyan", "purple"]  # Add more colors if needed
        first_row_color = "green"  # Change this to your preferred color
        for row in range(self.table1.rowCount()):
            ingredients = [
                self.table1.item(row, 0).text(),
                self.table2.item(row, 0).text(),
                self.table3.item(row, 0).text(),
                self.table4.item(row, 0).text(),
                self.table5.item(row, 0).text()
            ]
            versions = [
                self.table1.item(row, 1).text(),
                self.table2.item(row, 1).text(),
                self.table3.item(row, 1).text(),
                self.table4.item(row, 1).text(),
                self.table5.item(row, 1).text()
            ]

            if row == 0:  # This is the first row

                color = QColor(first_row_color)
                self.table1.item(row, 1).setForeground(color)
                self.table2.item(row, 1).setForeground(color)
                self.table3.item(row, 1).setForeground(color)
                self.table4.item(row, 1).setForeground(color)
                self.table5.item(row, 1).setForeground(color)

                my_font = QFont()
                my_font.setFamily("Arial")  # Set the font family to "Arial"
                my_font.setPointSize(8)  # Set the font size to 12 points
                my_font.setBold(True)  # Set the font to bold
                self.table1.item(row, 1).setFont(my_font)
                self.table2.item(row, 1).setFont(my_font)
                self.table3.item(row, 1).setFont(my_font)
                self.table4.item(row, 1).setFont(my_font)
                self.table5.item(row, 1).setFont(my_font)
            elif len(set(ingredients)) == 1 and len(
                    set(versions)) > 1:  # All ingredients are the same and versions are different
                unique_versions = list(set(versions))  # Get a list of unique versions
                color_dict = {version: colors[i % len(colors)] for i, version in
                              enumerate(unique_versions)}  # Assign a color to each unique version
                self.table1.item(row, 1).setForeground(QColor(color_dict[versions[0]]))
                self.table2.item(row, 1).setForeground(QColor(color_dict[versions[1]]))
                self.table3.item(row, 1).setForeground(QColor(color_dict[versions[2]]))
                self.table4.item(row, 1).setForeground(QColor(color_dict[versions[3]]))
                self.table5.item(row, 1).setForeground(QColor(color_dict[versions[4]]))

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.OS = "CENTOS"
        self.platform = "AP"

    def initUI(self):
        self.setGeometry(500,300,610,700)
        self.setWindowTitle("Check kit ingredients")

#Select Platform:
        self.label6 = QLabel("Select Platform:", self)
        self.label6.resize(80,12)
        self.label6.move(20, 32)

        self.checkBox5 = QCheckBox("AP",self)
        self.checkBox6 = QCheckBox("SP(2s)", self)
        self.checkBox7 = QCheckBox("SP(4s not enable)", self)
        self.checkBox5.setChecked(True) #Default

        self.checkBox5.move(120, 30)
        self.checkBox6.move(190, 30)
        self.checkBox7.move(270, 30)

        self.checkBox5.stateChanged.connect(self.get_check_box_status5)
        self.checkBox6.stateChanged.connect(self.get_check_box_status6)
        self.checkBox7.stateChanged.connect(self.get_check_box_status7)


#Select OS
        self.label3 = QLabel("Select an OS:", self)
        self.label3.resize(80,12)
        self.label3.move(20, 62)


        self.checkBox1 = QCheckBox("CentOS",self)
        self.checkBox2 = QCheckBox("Windows", self)
        self.checkBox3 = QCheckBox("ESXi", self)
        self.checkBox4 = QCheckBox("Redhat", self)
        self.checkBox1.setChecked(True) #Default

        self.checkBox1.move(120, 60)
        self.checkBox2.move(190, 60)
        self.checkBox3.move(270, 60)
        self.checkBox4.move(330, 60)

        self.checkBox1.stateChanged.connect(self.get_check_box_status1)
        self.checkBox2.stateChanged.connect(self.get_check_box_status2)
        self.checkBox3.stateChanged.connect(self.get_check_box_status3)
        self.checkBox4.stateChanged.connect(self.get_check_box_status4)

#Select a Kit
        self.bt1 = QPushButton("Select a Kit", self)
        #self.bt1.resize(65,20)
        self.bt1.move(490, 75)

        self.bt1.clicked.connect(self.show_dialog)



#print Kit details
        self.label1 = QLabel("Kit Name:", self)
        self.label1.move(20,95)

        #self.label2 = QLabel("NA", self)
        self.label2 = QLabel(
            '<a href="https://ubit-artifactory-ba.intel.com/artifactory/dcg-dea-srvplat-repos/Kits/" style="text-decoration: underline; color:blue;">Artifactory_Link</a>', self)
        self.label2.setOpenExternalLinks(True)
        self.label2.setFont(QFont('Arial', 10))
        self.label2.setStyleSheet("color:blue")
        self.label2.resize(200,16)
        self.label2.move(80, 95)

        self.table = QTableWidget(self)
        self.table.setGeometry(20, 120, 580, 370)
        # Set the table headers
        self.table.setRowCount(15)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Ingredient", "Version"])
        self.table.setColumnWidth(0, 100)
        self.table.setColumnWidth(1, 450)
        for i in range(0,15):
            self.table.setRowHeight(i, 5)

#Print 5 newest kit names
        self.label5 = QLabel("Newest 5 Kits Name:", self)
        self.label5.resize(210,12)
        self.label5.move(20, 510)
        self.text2 = QTextEdit("NA", self)
        self.text2.setGeometry(20, 540,250,100)

        self.button2 = QPushButton("Show name only", self)
        self.button2.move(100,640)
        self.button2.clicked.connect(self.show_5_kits)

        self.button3 = QPushButton("Details", self)
        self.button3.move(200,640)
        self.button3.clicked.connect(self.details_5kits)

#Compare 2 kits
        self.label4 = QLabel("Compare 2 kit:",self)
        self.label4.resize(70,12)
        self.label4.move(280, 510)

        self.text3 = QTextEdit(self)
        self.text3.setGeometry(280,540,210,20)
        self.text4 = QTextEdit(self)
        self.text4.setGeometry(280, 580, 210, 20)

        self.bt2 = QPushButton("Select Kit1", self)
        #self.bt1.resize(105,20)
        self.bt2.move(490, 538)
        self.bt3 = QPushButton("Select Kit2", self)
        #self.bt1.resize(65,20)
        self.bt3.move(490, 578)

        self.bt2.clicked.connect(self.get_kit1)
        self.bt3.clicked.connect(self.get_kit2)

        self.button = QPushButton("Compare2", self)
        self.button.move(490,640)
        self.button.clicked.connect(self.compare_2kits)



        self.show()

    def show_dialog(self):
        text = ""
        print("1---->", self.OS)
        print("2---->", self.platform)
        sender = self.sender()
        kits= ["BHS-GNR-AP-CENTOS-23.41.5.81"]
        if self.OS != "" and self.platform != "":
            kits = get_all_kits_name(self.OS, self.platform)


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
            kitDetail, kitPath = get_single_kit_info(text, self.platform)
            print("-=-=-=->",kitDetail)
            print("-=-=-=->", kitPath)
            if ok:
                #self.label2.setText(text)
                self.label2.setText(
                    f'<a href="{kitPath}" style="text-decoration: underline; color:blue;">{text}</a>')
                #self.text.clear()
            else:
                self.label2.clear()

            # kitDetail, kitPath = get_single_kit_info(text, self.platform)
            # print("-=-=-=->",kitDetail)
            # print("-=-=-=->", kitPath)

        self.table.clear()
        self.table.setHorizontalHeaderLabels(["Ingredient", "Version"])
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
        if self.OS != "":
            kits = get_all_kits_name(self.OS, self.platform)

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
        if self.OS != "":
            kits = get_all_kits_name(self.OS, self.platform)

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
        print("************>", kitID1, self.platform)
        kitID2 = self.text4.toPlainText()
        print("************>", kitID2)
        kitDict1, kitPath = get_single_kit_info(kitID1, self.platform)
        kitDict2, kitPath = get_single_kit_info(kitID2, self.platform)
        #kitDict1 = getKitDetails(kitID1)
        #kitDict2 = getKitDetails(kitID2)
        print("kit1--->", kitDict1)
        print("kit2--->", kitDict2)

        window = TableWindow(kitDict1, kitDict2, kitID1, kitID2)
        window.exec_()

    def show_5_kits(self):
        print("---> show 5 newest kits", self.OS , self.platform)
        kits = self.text2.toPlainText()
        self.text2.clear()
        kits = get_all_kits_name(self.OS, self.platform)
        print(kits[0:5])
        kits.reverse()
        print(kits[0:5])
        for i in range(0,5):
            self.text2.append(kits[i])

    def clear_5kits(self):
        sender = self.sender()
        if sender == self.button3:
            self.text2.clear()

    def details_5kits(self):
        print("---> details 5 newest kits", self.OS, self.platform)
        self.text2.clear()
        kits = self.text2.toPlainText()

        if kits == "NA" or kits == "":
            self.text2.clear()
            kits = get_all_kits_name(self.OS, self.platform)
            print(kits[0:5])
            kits.reverse()
            print(kits[0:5])
            for i in range(0, 5):
                self.text2.append(kits[i])
        print("defails ", kits[0:5])
        #To set the kit name at head position
        kitDict1 = {'Kit Name:': kits[0]}
        kitDict2 = {'Kit Name:': kits[1]}
        kitDict3 = {'Kit Name:': kits[2]}
        kitDict4 = {'Kit Name:': kits[3]}
        kitDict5 = {'Kit Name:': kits[4]}
        #kits=["BHS-GNR-AP-WIN-23.42.2.93","BHS-GNR-AP-WIN-23.42.2.93","BHS-GNR-AP-WIN-23.42.2.93"]
        kit1, kitPath1 = get_single_kit_info(kits[0], self.platform)
        kit2, kitPath2 = get_single_kit_info(kits[1], self.platform)
        kit3, kitPath3 = get_single_kit_info(kits[2], self.platform)
        kit4, kitPath4 = get_single_kit_info(kits[3], self.platform)
        kit5, kitPath5 = get_single_kit_info(kits[4], self.platform)
        kitDict1.update(kit1)
        kitDict2.update(kit2)
        kitDict3.update(kit3)
        kitDict4.update(kit4)
        kitDict5.update(kit5)

        print("update kit----->", kitDict4)
        print("update kit----->", kitDict5)
        window = TableWindow2(kitDict1, kitDict2, kitDict3, kitDict4, kitDict5)
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

    def get_check_box_status5(self):
        if self.checkBox5.checkState() == Qt.Checked:
            print("User select AP")
            self.platform = "AP"
            self.checkBox6.setChecked(False)
            self.checkBox7.setChecked(False)
    def get_check_box_status6(self):
        if self.checkBox6.checkState() == Qt.Checked:
            print("User select SP(2s)")
            self.platform = "SP"
            self.checkBox5.setChecked(False)
            self.checkBox7.setChecked(False)
    def get_check_box_status7(self):
        if self.checkBox7.checkState() == Qt.Checked:
            print("User select SP(4s)")
            self.platform = "SP(4s)"
            self.checkBox5.setChecked(False)
            self.checkBox6.setChecked(False)


if __name__ =='__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app=QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())