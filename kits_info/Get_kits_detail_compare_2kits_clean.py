import os
import sys
from urllib.request import urlopen
from xml.etree import ElementTree as ET
from colorama import init
init(autoreset=True)

ingredientsList = ['IFWI',"BMC","CPLD","CPLD_PFR","LAN","QAT","SAF","SAF_Blob","SGX","SGXFVT_Tool","VROC_UEFI","dlb","on_demand_agent","CentOS"]

def downloadKitXml(kitName):
    kitID = kitName
    urlPath = f"https://ubit-artifactory-ba.intel.com/artifactory/dcg-dea-srvplat-repos/Kits/BHS-GNR-AP-CentOS/{kitID}/Documents/{kitID}.xml"
    cmd = f'curl -f -u caifulai:My@920118   -X GET {urlPath} --output C:\\00000000000\OneBKC_Kit_info\{kitID}.xml'
    print("---->", cmd)
    os.system(cmd)
    localXml=os.path.join(f"C:\\00000000000\OneBKC_Kit_info\{kitID}.xml")
    print("\n\033[1;32mKit Name: %-*s \033[0m"%(40,localXml))

def getKitDetails(kitName):
    result={}
    kitID = kitName
    urlPath = f"https://ubit-artifactory-ba.intel.com/artifactory/dcg-dea-srvplat-repos/Kits/BHS-GNR-AP-CentOS/{kitID}/Documents/{kitID}.xml"
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


#def twoKitsCompare(kitName1, kitName2):
def twoKitsCompare(kitName1, kitName2):
    kitID1=kitName1
    kitID2=kitName2
    kitDict1=getKitDetails(kitID1)
    kitDict2=getKitDetails(kitID2)
    print("\033[1;32mKit Name(Candidate): %-*s |%-*s\033[0m" % (82, kitID1, 1, ""),"\033[1;33mKit Name(Newer): %-*s |%-*s\033[0m" % (91, kitID2, 1, ""))
    for key in kitDict1.keys():
        if kitDict1[key] == kitDict2[key]:
            print("ingredient: %-*s Version: %-*s  |%-*s" % (20, key, 60, kitDict1[key], 1, ""), "ingredient: %-*s Version: %-*s  |%-*s" % (20, key, 65, kitDict2[key], 20, ""))
        else:
            print("ingredient: %-*s Version: \033[0;31m%-*s\033[0m  |%-*s" % (20, key, 62, kitDict1[key], 1, ""),
                  "ingredient: %-*s Version: \033[0;31m%-*s\033[0m  |%-*s" % (20, key, 62, kitDict2[key], 20, ""))

if __name__ == '__main__':
    twoKitsCompare(sys.argv[1], sys.argv[2])
    #twoKitsCompare("BHS-GNR-AP-CENTOS-23.13.5.151","BHS-GNR-AP-CENTOS-23.13.5.130")