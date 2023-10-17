import os
import sys
from urllib.request import urlopen
from xml.etree import ElementTree as ET
from PyQt5.QtWidgets import QMessageBox,QApplication
from urllib.request import urlopen
from urllib.error import URLError


def get_single_kit_info(kitID, platform):
    ingredients = {}
    print("\n\033[1;32mKit Name: %-*s \033[0m" % (40, kitID))
    if "CENTOS" in kitID:
        urlPath = f"https://ubit-artifactory-sh.intel.com/artifactory/dcg-dea-srvplat-repos/Kits/BHS-GNR-{platform}-CentOS/{kitID}/Documents/{kitID}.xml"
        ingredientsList = ['IFWI', "BMC", "CPLD", "CPLD_PFR", "CentOS","LAN", "QAT", "SAF", "SAF_Blob", "SGX", "SGXFVT_Tool",
                           "VROC_UEFI", "dlb", "on_demand_agent"]
    elif "WIN" in kitID:
        urlPath = f"https://ubit-artifactory-sh.intel.com/artifactory/dcg-dea-srvplat-repos/Kits/BHS-GNR-{platform}-WIN/{kitID}/Documents/{kitID}.xml"
        ingredientsList = ['IFWI', "BMC", "CPLD", "CPLD_PFR", "BaseWIM-20H2","LAN", "QAT", "SAF", "SAF_Blob", "SGX", "SGXFVT_Tool",
                           "VROC_UEFI", "dlb", "on_demand_agent"]
    elif "ESXI" in kitID:
        urlPath = f"https://ubit-artifactory-ba.intel.com/artifactory/dcg-dea-srvplat-repos/Kits/BHS-GNR-{platform}-ESXI/{kitID}/Documents/{kitID}.xml"
        ingredientsList = ['IFWI', "BMC", "CPLD", "CPLD_PFR",  "VMware","LAN", "QAT", "SAF", "SAF_Blob", "SGX", "SGXFVT_Tool",
                           "VROC_UEFI", "dlb", "on_demand_agent"]
    else:
        urlPath = f"https://ubit-artifactory-sh.intel.com/artifactory/dcg-dea-srvplat-repos/Kits/BHS-GNR-{platform}-RHEL/{kitID}/Documents/{kitID}.xml"
        ingredientsList = ['IFWI', "BMC", "CPLD", "CPLD_PFR", "RHEL","LAN", "QAT", "SAF", "SAF_Blob", "SGX", "SGXFVT_Tool",
                           "VROC_UEFI", "dlb", "on_demand_agent"]
    print(urlPath)
    try:
        kitXml = urlopen(urlPath)
    except URLError:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(f"URL does not exist, the kits may be deleted! \nkit: {kitID}  \nurl:{urlPath}  \nProgram will exit now!")
        msg.setWindowTitle("URL Error")
        msg.exec_()
        sys.exit(1)

    #kitXml = urlopen(urlPath)
    kitContent = kitXml.read().decode('utf-8')
    #print(kitContent)
    kitXmlRoot = ET.fromstring(kitContent)


    for elem in kitXmlRoot:
        if elem.get("name") is not None :
            #print("find a elem with a name info")
            for item in ingredientsList:
                if elem.get("name") == item:
                   ingredients[item] = elem.attrib['version']
    return ingredients


def getKitDetails(kitID):
    if "CENTOS" in kitID:
        urlPath = f"https://ubit-artifactory-sh.intel.com/artifactory/dcg-dea-srvplat-repos/Kits/BHS-GNR-AP-CentOS/{kitID}/Documents/{kitID}.xml"
        ingredientsList = ['IFWI', "BMC", "CPLD", "CPLD_PFR", "CentOS","LAN", "QAT", "SAF", "SAF_Blob", "SGX", "SGXFVT_Tool",
                           "VROC_UEFI", "dlb", "on_demand_agent"]
    elif "WIN" in kitID:
        urlPath = f"https://ubit-artifactory-sh.intel.com/artifactory/dcg-dea-srvplat-repos/Kits/BHS-GNR-AP-WIN/{kitID}/Documents/{kitID}.xml"
        ingredientsList = ['IFWI', "BMC", "CPLD", "CPLD_PFR", "BaseWIM-20H2","LAN", "QAT", "SAF", "SAF_Blob", "SGX", "SGXFVT_Tool",
                           "VROC_UEFI", "dlb", "on_demand_agent"]
    elif "ESXI" in kitID:
        urlPath = f"https://ubit-artifactory-ba.intel.com/artifactory/dcg-dea-srvplat-repos/Kits/BHS-GNR-AP-ESXI/{kitID}/Documents/{kitID}.xml"
        ingredientsList = ['IFWI', "BMC", "CPLD", "CPLD_PFR",  "VMware","LAN", "QAT", "SAF", "SAF_Blob", "SGX", "SGXFVT_Tool",
                           "VROC_UEFI", "dlb", "on_demand_agent"]
    else:
        urlPath = f"https://ubit-artifactory-sh.intel.com/artifactory/dcg-dea-srvplat-repos/Kits/BHS-GNR-AP-RHEL/{kitID}/Documents/{kitID}.xml"
        ingredientsList = ['IFWI', "BMC", "CPLD", "CPLD_PFR", "RHEL","LAN", "QAT", "SAF", "SAF_Blob", "SGX", "SGXFVT_Tool",
                           "VROC_UEFI", "dlb", "on_demand_agent"]

    result={}
    print("---->",urlPath)
    kitXml = urlopen(urlPath)
    kitContent = kitXml.read().decode('utf-8')
    kitXmlRoot = ET.fromstring(kitContent)
    for elem in kitXmlRoot:
        if elem.get("name") is not None :
            #print("find a elem with a name info")
            for item in ingredientsList:
                if elem.get("name") == item:
                    result[elem.attrib['ingredient']] = elem.attrib['version']
    return result

def get_all_kits_name(OS, platform):
    print("get all kits name:", OS, platform)
    urlPath = f"https://ubit-artifactory-ba.intel.com/artifactory/dcg-dea-srvplat-repos/Kits/BHS-GNR-{platform}-{OS}/"
    kitAll = urlopen(urlPath)
    kits = kitAll.read().decode('utf-8')
    kits=kits.split(' ')
    kitsList=[]
    for item in kits:
        if f"BHS-GNR-{platform}-" in item and "-23" in item:
            #print(item)
            start=item.find(r'"BHS-')
            end = item.find(r'/">BHS')
            kitsList.append(item[(start+1):end])
    return kitsList

if __name__ == "__main__":
    app = QApplication([])
    kitID1 = "BHS-GNR-AP-CENTOS-23.41.5.81"
    kitID2= "BHS-GNR-AP-WIN-23.41.5.83"
    kitID3 = "BHS-GNR-SP-ESXI-23.42.1.64"
    kitID3 = "BHS-GNR-SP-RHEL-23.41.7.56"
    #kitID = "BHS-GNR-AP-WIN-23.01.5.231"
    print(get_single_kit_info(kitID3,"SP"))
    print(getKitDetails(kitID1))