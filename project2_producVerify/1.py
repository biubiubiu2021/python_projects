import os
import time
count = 0
error_count=0
while count < 100:
    os.popen("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.2.1\\bin\pycharm.bat")
    count = count + 1
    print("-------->", count)
    result = os.popen("tasklist.exe /M JVM.dll")
    if "java" in result.read():
        print("pycharm is opened!")
        time.sleep(300)
        result2 = os.popen("tasklist.exe /M JVM.dll")
        if "java" in result2.read():
            print("pycharm is still working after 100 seconds!")
            os.popen("taskkill.exe /F /IM java.exe")
            result3 = os.popen("tasklist.exe /M JVM.dll")
            time.sleep(1)
            if "java" not in result3.read():
                print("pycharm is closed after 100 seconds!")
                time.sleep(20)
        else:
            print("Pycharm crashed with issue!")
            error_count = error_count+1
            print("=========================================================>",error_count)
            