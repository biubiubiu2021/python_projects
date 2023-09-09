# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os,time,string,random
import tkinter
import qrcode

from pystrich.ean13 import EAN13Encoder
import tkinter.filedialog
import tkinter.messagebox
from tkinter import *
from string import digits

number = '1234567890'
letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
allis = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'
randstr = []
fourth = []
fifth = []
randfir = ""
randsec = ""
randthr = ""
str_one = ""
strone = ""
strtwo = ""
nextcard = ""
userput = ""
nres_letter = ""



root = tkinter.Tk()
root.geometry('800x600+100+100')

def input_validation(insel):
    if str.isdigit(insel):
        if insel == 0:
            print("\033[1;31[0m Exist the system! \033[0m")
            return 0
        else:
            return int(insel)
    else:
        print("\033[1;31;40m  invalid input! pls check  \033[0m")
        return 0

def mkdir(path):
    isExist = os.path.exists(path)
    if not isExist:
        print('"',path, '"', "not exist! Create a new folder")
        os.mkdir(path)
        print(path, "successfully created!")
    else:
        print('"',path, '"',"already exist!")
        return

def openfile(filename):
    f=open(filename, 'r')
    content = f.read()
    f.close()
    return content


def inputbox(showstr, showorder, length):
    instr = input(showstr)
    if len(instr) != 0:
        #Three kinds of verification, 1,number,  2,string + length , 3, number +length
        if showorder == 1:  #number
            if instr.isdigit():
                print("this is a number")
                if instr == '0':
                    print("\033[1;31;40m input is 0, pls re-try! \033[0m")
                    return '0'
                else:
                    return instr
            else:
                print("\033[1;31;40m input is not a valid munber, pls re-try! \033[0m")
                return '0'
        if showorder == 2: #letter+length
            if instr.isalpha():
                print("this is a letter")
                if len(instr) != length:
                    print("\033[1;31;40m pls input",length, " letters, pls re-try! \033[0m")
                    return '0'
                else:
                    return instr
            else:
                print("\033[1;31;40m input is not a valid letter, pls re-try! \033[0m")
                return "0"
        if showorder == 3:#number+length
            if str.isdigit(instr):
                print("this is a number")
                if len(instr) != length:
                    print("\033[1;31;40m pls input",length, " number, pls re-try! \033[0m")
                    return '0'
                else:
                    return instr
            else:
                print("\033[1;31;40m input is not a valid munber, pls re-try! \033[0m")
                return '0'
    else:
        print("\033[1;31;40m Empty imput, pls re-try! \033[0m")
        return 0

def wfile(sstr,sfile, typeis, smsg, datapath):
    mkdir(datapath)
    datafile = datapath + '\\' + sfile
    file = open(datafile, 'w')
    wrlist = sstr
    pdata = ''
    wdata = ''
    for i in range(len(sstr)):
        wdata = str(wrlist[i].replace('[',"").replace(']',""))
        file.write(wdata)
        pdata = pdata + wdata
    file.close()
    print("\033[1;31;40m The security code is:\n",pdata, "\033[0m")
    if typeis != 'no':
        root.attributes("-topmost", True)
        root.geometry("800x600")
        root.withdraw()
        root.quit()
        tkinter.messagebox.showinfo("Note:", smsg + str(len(sstr)) + '\n scode file saved in:\n' + datafile)
        time.sleep(5)


def scode1(schoice):
    number = '1234567890'

    randstr = []
    incount = inputbox("\033[1;32m 请输入您要生成的防伪码数量: \033[0m", 1, 0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32m 请输入您要生成的防伪码数量: \033[0m", 1, 0)
    randstr.clear()
    for j in range(int(incount)):
        randfir = ""
        for i in range(6):
            randfir = randfir + random.choice(number)
        randfir = randfir + "\n"
        randstr.append(randfir)
    print("----->",incount)
    wfile(randstr,'scode' + str(schoice)+'.txt', "yes", f"Already generated  6 bits codes, total:",'.\\files')

def scode2(schoice):
    order_start = inputbox("\033[1;32m 请输入系列产品的数字起始号（3位）: \033[0m", 3,3) # showorder =3 means number+lenght, length=3, 3 bits
    while int(order_start) == 0:
        order_start = inputbox("\033[1;32m 请输入系列产品的数字起始号（3位）: \033[0m", 3, 3)

    order_count = inputbox("\033[1;32m 请输入产品系列的数量: \033[0m", 1, 0) # showder=3 means number only, but length=0 means no length limitation
    while int(order_count) < 1 or int(order_count) > 9999: #the number of order should be in 1-9999
        order_count = inputbox("\033[1;32m 请输入产品系列的数量: \033[0m", 1, 0)

    incount = inputbox("\033[1;32m 请输入要生成的防伪码的数量: \033[0m", 1, 0) # showder=3 means number only,
    while int(incount) ==0:
        print("输入不正确，清请输入大于0的整数！")
        incount = inputbox("\033[1;32m 请输入要生成的防伪码的数量: \033[0m", 1, 0)

    randstr.clear()
    for m in range(int(order_count)): #产品系列的数量，假如数字起始号order_start=100，产品系列的数量order_cound=3, 则 三个系列的起始号分别为100，101，102
        for j in range(int(incount)):#incount位产品防伪码数量,
            randfir = ""
            for i in range(6):
                randfir = randfir + random.choice(number)  #每次生成一位随机数，然后添加到防伪码，一共生成6位，组成一个6位防伪码
            randstr.append(str(int(order_start)+m) + randfir +"\n")  #order_cound +m, 假使第一个数字起始号位123， 则第二个位123+1=124， 完整的防伪码= 3位系列起始号（会安装产品系类数量+1变化）+6位防伪码

    wfile(randstr,"scode"+str(schoice)+".txt","","已生成9位系列产品防伪码共计：",".\\files")

def scode3(schoice):
    incount = inputbox("\033[1;32m 请输入要生成的25位混合产品序列号数量（25位）: \033[0m", 1,0)
    while int(incount) == 0:
        incount = inputbox("\033[1;32m 请输入要生成的25位混合产品序列号数量（25位）: \033[0m", 1, 0)
    randstr.clear()
    for j in range(int(incount)):
        randfir=""
        for i in range(25):
            randfir = randfir + random.choice(letter) #get 25 bits data
        randstr.append(randfir[0:5]+"-"+randfir[5:10]+"-"+randfir[10:15]+"-"+randfir[15:20]+"-"+randfir[20:25]+"\n")

    wfile(randstr, "scode" + str(schoice) + ".txt", "", "已生成25位混合产品序列号共计：", ".\\files")


def mainmenu():
    print("""\033[1;35m
        ********************************************************************************
                                        企业编码生成系统
        ********************************************************************************
        1. 生成6位数字防伪编码（213563型）
        2. 生成9位系列产品数字防伪编码（879-335439型）
        3. 生成25位混合产品序列号
        4. 生成含数据分析功能的防伪编码
        5. 智能批量生成带数据分析功能的防伪编码
        6. 后续补加生成防伪码
        7. EAN-13 条形码批量生成
        8. 二维码批量输出
        9. 企业粉丝防伪码抽奖
        0. 退出系统
        ********************************************************************************
        说明： 通过数字选择菜单
        ********************************************************************************     
    \033[0m""")

def main():
    i=0
    while i < 9:
        mainmenu()
        choice = input("\033[1;32m Pls select a function: \033[0m")
        if len(choice) != 0:
            choice = input_validation(choice)
            print("---->",choice)
            if choice == 1:
                print("it is !!!")
                scode1(choice)
            if choice == 2:
                scode2(choice)
            if choice == 3:
                scode3(choice)
            if choice == 4:
                scode4(choice)
            if choice == 5:
                scode5(choice)
            if choice == 6:
                scode6(choice)
            if choice == 7:
                scode7(choice)
            if choice == 8:
                scode8(choice)
            if choice == 9:
                scode9(choice)
            if choice == 0:
                i = 10
                print("\033[1;21;42m  Exist the system! \033[0m")
                break
        else:
            print("\033[1;21;42m  Exist the system! \033[0m")
            break


if __name__ == '__main__':

    mkdir('.\\files')
    #print(openfile('D:\\python_project\\producVerify\main.py'))
    #print(inputbox("pls input:  ",3,3))
    #wfile("ABCD","scode1.txt",'yes', 'Saved files','.\\test')
    main()
    #scode1(1)
