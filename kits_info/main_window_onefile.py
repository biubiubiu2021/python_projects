from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QInputDialog,QTextBrowser,QTextEdit,QCheckBox
import sys
#from get_all_kits_name import get_all_kits_name
#from Get_kits_detail_single_kit import get_single_kit_info
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from urllib.request import urlopen
import os
import sys
from urllib.request import urlopen
from xml.etree import ElementTree as ET


def get_all_kits_name(OS):
    print("get all kits name:", OS)
    urlPath = f"https://ubit-artifactory-ba.intel.com/artifactory/dcg-dea-srvplat-repos/Kits/BHS-GNR-AP-{OS}/"
    kitAll = urlopen(urlPath)
    kits = kitAll.read().decode('utf-8')
    kits=kits.split(' ')
    kitsList=[]
    for item in kits:
        if "BHS-GNR-AP-" in item and "-23" in item:
            #print(item)
            start=item.find(r'"BHS-')
            end = item.find(r'/">BHS')
            kitsList.append(item[(start+1):end])
    return kitsList

def get_single_kit_info(kitID):
    info = []
    print("\n\033[1;32mKit Name: %-*s \033[0m" % (40, kitID))
    if "CENTOS" in kitID:
        urlPath = f"https://ubit-artifactory-sh.intel.com/artifactory/dcg-dea-srvplat-repos/Kits/BHS-GNR-AP-CentOS/{kitID}/Documents/{kitID}.xml"
        ingredientsList = ['IFWI', "BMC", "CPLD", "CPLD_PFR", "LAN", "QAT", "SAF", "SAF_Blob", "SGX", "SGXFVT_Tool",
                           "VROC_UEFI", "dlb", "on_demand_agent"]
    elif "WIN" in kitID:
        urlPath = f"https://ubit-artifactory-sh.intel.com/artifactory/dcg-dea-srvplat-repos/Kits/BHS-GNR-AP-WIN/{kitID}/Documents/{kitID}.xml"
        ingredientsList = ['IFWI', "BMC", "CPLD", "CPLD_PFR", "LAN", "QAT", "SAF", "SAF_Blob", "SGX", "SGXFVT_Tool",
                           "VROC_UEFI", "dlb", "on_demand_agent", "BaseWIM-20H2"]
    elif "ESXI" in kitID:
        urlPath = f"https://ubit-artifactory-ba.intel.com/artifactory/dcg-dea-srvplat-repos/Kits/BHS-GNR-AP-ESXI/{kitID}/Documents/{kitID}.xml"
        ingredientsList = ['IFWI', "BMC", "CPLD", "CPLD_PFR", "LAN", "QAT", "SAF", "SAF_Blob", "SGX", "SGXFVT_Tool",
                           "VROC_UEFI", "dlb", "on_demand_agent", "VMware"]
    else:
        urlPath = f"https://ubit-artifactory-sh.intel.com/artifactory/dcg-dea-srvplat-repos/Kits/BHS-GNR-AP-RHEL/{kitID}/Documents/{kitID}.xml"
        ingredientsList = ['IFWI', "BMC", "CPLD", "CPLD_PFR", "LAN", "QAT", "SAF", "SAF_Blob", "SGX", "SGXFVT_Tool",
                           "VROC_UEFI", "dlb", "on_demand_agent"]
    print(urlPath)
    kitXml = urlopen(urlPath)
    kitContent = kitXml.read().decode('utf-8')
    #print(kitContent)
    kitXmlRoot = ET.fromstring(kitContent)


    for elem in kitXmlRoot:
        if elem.get("name") is not None :
            #print("find a elem with a name info")
            for item in ingredientsList:
                if elem.get("name") == item:
                    #print("ingredient: %-*s Version: %s" %(20, elem.attrib['ingredient'],elem.attrib['version']))
                    blanks = 40 - len(elem.attrib['ingredient'])
                    info_string = "ingredient: " + elem.attrib['ingredient'] + " "*blanks + "Version: "+elem.attrib['version']
                    info.append(info_string)
    return info


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.OS = "CENTOS"

    def initUI(self):
        self.setGeometry(300,500,500,500)
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