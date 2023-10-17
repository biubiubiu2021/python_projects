import os
from urllib.request import urlopen
from xml.etree import ElementTree as ET

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
    print(get_all_kits_name("CentOS","AP"))
    print(get_all_kits_name("ESXI","SP"))
    print(get_all_kits_name("WIN","AP"))
    print(get_all_kits_name("RHEL","SP"))


