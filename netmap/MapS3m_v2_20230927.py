import os

netDriverLebel = ['Z:', 'Y:', 'X:', 'W:', 'V:', 'U:', 'T:', 'S:']

def get_netDriveLebel():
    lebelList = []
    result = os.popen("net use |findstr \\")
    result=result.read().split()
    for i in range(len(result)):
        if result[i] in netDriverLebel:
            lebelList.append(result[i])
    return lebelList


def get_netMap():
    netMap = {}
    result = os.popen("net use |findstr \\")
    result=result.read().split()
    #print(result)
    for i in range(len(result)):
        if "s3m_fw" in result[i]:
            print("\033[0;31;48m Find the old S3m NetDriveMap!  \033[0m",result[i-1],result[i])
            netMap.update({result[i-1]:result[i]})
    return netMap

def deleteNetMap(netMap):

    for i,j in netMap.items():
        print("\033[1;33;40m Delete the old S3m NetDriveMap!  \033[0m",i,j)
        cmd = f"net use /delete {i}"
        restr=os.popen(cmd).read()
        if "was deleted successfully" in restr:
            print("------->",i,j,"was deleted successfully!")
        else:
            print("No Such netDrive mounted")

def mount_netDrive(path):
    if path == "":
        print("\033[1;31;40m No NetDrive PATH!  \033[0m")
    else:
        lebelList = get_netDriveLebel()
        for i in netDriverLebel:
            if i not in lebelList:
                cmd = f"net use {i} {path} /user:ccr\caifulai My@920118 /p:yes"
                print("\033[1;35;48m Setting the S3M PATH!  \033[0m")
                restr = os.popen(cmd).read()
                if "The command completed successfully" in restr:
                    print(i,path, "\033[1;30;42m S3M net drive mapping completed successfully! \033[0m")
                break
            else:
                print("No enaough drive lable! Pls contact Caifu!")

if __name__ == "__main__":
    path = r"\\samba.fm.intel.com\nfs\site\disks\cpuemu.srvr10nm.tools.1\s3m_fw"
    netMap = get_netMap()
    deleteNetMap(netMap)
    get_netDriveLebel()
    mount_netDrive(path)