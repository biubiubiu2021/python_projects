import os
import sys
from urllib.request import urlopen
from xml.etree import ElementTree as ET



def get_single_kit_info(kitID):
    info = []
    ingredients = {}
    print("\n\033[1;32mKit Name: %-*s \033[0m" % (40, kitID))
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
                   ingredients[item] = elem.attrib['version']
    return ingredients


def getKitDetails(kitName):
    if "CENTOS" in kitName:
        urlPath = f"https://ubit-artifactory-sh.intel.com/artifactory/dcg-dea-srvplat-repos/Kits/BHS-GNR-AP-CentOS/{kitID}/Documents/{kitID}.xml"
        ingredientsList = ['IFWI', "BMC", "CPLD", "CPLD_PFR", "CentOS","LAN", "QAT", "SAF", "SAF_Blob", "SGX", "SGXFVT_Tool",
                           "VROC_UEFI", "dlb", "on_demand_agent"]
    elif "WIN" in kitName:
        urlPath = f"https://ubit-artifactory-sh.intel.com/artifactory/dcg-dea-srvplat-repos/Kits/BHS-GNR-AP-WIN/{kitID}/Documents/{kitID}.xml"
        ingredientsList = ['IFWI', "BMC", "CPLD", "CPLD_PFR", "BaseWIM-20H2","LAN", "QAT", "SAF", "SAF_Blob", "SGX", "SGXFVT_Tool",
                           "VROC_UEFI", "dlb", "on_demand_agent"]
    elif "ESXI" in kitName:
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



if __name__ == "__main__":
    kitID = "BHS-GNR-AP-CENTOS-23.41.5.81"
    kitID = "BHS-GNR-AP-WIN-23.41.5.83"
    kitID = "BHS-GNR-AP-ESXI-23.41.6.132"
    #kitID = "BHS-GNR-AP-WIN-23.01.5.231"
    print(get_single_kit_info(kitID))
    print(getKitDetails(kitID))