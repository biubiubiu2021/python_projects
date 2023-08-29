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
i=0
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


def inputbox(showstr,showorder, length):
    instr = input(showstr)
    if len(instr) != 0:
        if showorder ==1:
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
        if showorder ==2:
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
        if showorder ==3:
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
    print("\033[1;31;40m The security code is:",pdata, "\033[0m")
    if typeis != 'no':
        root.withdraw()
        tkinter.messagebox.showinfo("Note:", smsg + str(len(sstr)) + '\n scode file saved in:\n' + datafile)



def main():
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

if __name__ == '__main__':
    mkdir('D:\python_project\project2_producVerify')
    #print(openfile('D:\\python_project\\producVerify\main.py'))
    #print(inputbox("pls input:  ",3,3))
    #wfile("ABCD","scode1.txt",'yes', 'Saved files','D:\python_project\project2_producVerify\\test')
    main()
