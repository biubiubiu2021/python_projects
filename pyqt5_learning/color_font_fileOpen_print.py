from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QFontDialog,QColorDialog,QTextEdit,QFileDialog,QDialog
import sys
from PyQt5.QtPrintSupport import QPageSetupDialog, QPrintDialog,QPrinter
#QPageSetupDialog涉及页面设置的, QPrintDialog涉及打印
#QPrinter类是PyQt的打印主要使用，即打印类。大量和打印相关的函数均会涉及到该类。
#虚拟打印机，通过与这台打印交互达到控制本地实际打印机的功能
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.printer = QPrinter()
        #因为下面代码中QPageSetupDialog、QPrintDialog涉及到QPrinter()对象，所以将其在类初始化的时候生成，便于函数的调用。

    def initUI(self):
        self.setGeometry(300,300,500,400)
        self.setWindowTitle("hahahah")

        self.text = QTextEdit(self)
        self.text.setGeometry(20,20,300,370)

        self.button1 = QPushButton("open file", self)
        self.button1.move(350,20)
        self.button2 = QPushButton("open files", self)
        self.button2.move(350,70)
        self.button3 = QPushButton("save file", self)
        self.button3.move(350,120)
        self.button4 = QPushButton("page setting", self)
        self.button4.move(350,170)
        self.button5 = QPushButton("print file", self)
        self.button5.move(350,220)
        self.button6 = QPushButton("select font", self)
        self.button6.move(350, 270)
        self.button7 = QPushButton("select color", self)
        self.button7.move(350,320)

        self.button1.clicked.connect(self.open_file)
        self.button2.clicked.connect(self.open_files)
        self.button3.clicked.connect(self.save_file)
        self.button4.clicked.connect(self.page_settings)
        self.button5.clicked.connect(self.print_dialog)

        self.button6.clicked.connect(self.select_font)
        self.button7.clicked.connect(self.select_color)

        self.show()

    def open_file(self):
        fname = QFileDialog.getOpenFileName(self,"open file:","./",("Text(*.txt *.text)"))
        #QFileDialog对话框。 getOpenFileName()方法中的第一个字符串是标题。第二个字符串指定对话框工作目录。默认情况下，文件过滤器设置为所有文件（*），即不限制打开文件的类型。
        print("--->",fname)
        print(type(fname))
        #---> ('C:/Users/caifulai/OneDrive - Intel Corporation/Desktop/temp/Stability_Idle_L.txt', 'Text(*.txt *.text)')
        #<class 'tuple'> 返回值类型是元组
        if fname[0]:
            with open(fname[0], 'r', encoding='gb18030',errors="ignore") as f:
                self.text.setText(f.read())
            #读取所选择的文件名，并将文本编辑小部件的内容设置为文件读取的内容。这里提一下使用with语句来自动帮我们调用close()方法，
            # 避免由于文件读写时产生IOError，导致close()不会调用，需要try ... finally来实现的不便。
            #http://www.xdbcb8.com/archives/1835.html

    def open_files(self):
        fnames =  QFileDialog.getOpenFileNames(self,"open files","./",("Text(*.txt *.text)"))
        print("***>",fnames)
        print(type(fnames))
        #***> (['C:/Users/caifulai/PycharmProjects/python_projects/pyqt5_learning/666.txt', 'C:/Users/caifulai/PycharmProjects/python_projects/pyqt5_learning/test.txt'], 'Text(*.txt *.text)')
        #<class 'tuple'>
        #返回值是元组。元组的第0个元素则是列表
        if fnames[0]:
            for fname in fnames[0]:
                with open(fname,'r', encoding='gb18030', errors="ignore") as f:
                    self.text.append(f.read())
                    #QTextEdit的append方法，让每次显示的内容均会存留在QTextEdit上

    def save_file(self):
        filename = QFileDialog.getSaveFileName(self,"save file","./",("Text(*.txt *.text)"))
        #getSaveFileName()具体的用法与getOpenFileNames()类似，
        if filename[0]:
            with open(filename[0], 'w', encoding="gb18030", errors='ignore') as f:
                f.write(self.text.toPlainText())
                #使用write函数将QTextEdit的内容保存在文件中。获取的QTextEdit的内容可以使用这个函数toPlainText()。

    def page_settings(self):
        printsetdialog = QPageSetupDialog(self.printer,self)
        printsetdialog.exec_()#执行确认的页面设置信息

    def print_dialog(self):
        printsetdialog = QPrintDialog(self.printer,self)
        if QDialog.Accepted == printsetdialog.exec_():
            self.text.print(self.printer)
        #调用QPrintDialog准备进行打印
        #QPrintDialog类提供了一个用于指定打印机配置的对话框。对话框允许用户更改文档相关设置，如纸张尺寸和方向，打印类型（颜色或灰度），页面范围和打印份数。
        #还提供控制以使用户可以从可用的打印机中进行选择，包括任何配置的网络打印机

    def select_color(self):
        color = QColorDialog.getColor()
        print("--->",color)
        #---> <PyQt5.QtGui.QColor object at 0x0000026150F79820>
        if color.isValid():
            self.text.setTextColor(color)

    def select_font(self):
        font, ok = QFontDialog.getFont()
        #字体对话框。 getFont()方法返回字体名称以及用户点击按钮的状态。如果用户点击Ok，则等于True
        print("--->", font, ok)
        #---> <PyQt5.QtGui.QFont object at 0x0000026150F79820> True
        if ok:
            #self.text.setFont(font) #设置全局的字体
            self.text.setCurrentFont(font)



if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())