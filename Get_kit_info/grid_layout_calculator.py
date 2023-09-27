import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QGridLayout,QLCDNumber

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        print("1--->",grid.rowCount(),grid.columnCount())
        #创建QGridLayout的实例并将其设置为应用程序窗口的布局。

        self.setGeometry(300,300,400,300)
        self.setWindowTitle("Calculator")

        self.lcd = QLCDNumber()
        grid.addWidget(self.lcd,0,0,3,0)#addWidget (self, QWidget, row, column, rowSpan, columnSpan, Qt.Alignment alignment = 0)
        #addwidget方法第一个参数是添加的控件对象,后面的（0，0）表示位置坐标为（0，0），即控件左上角坐标为（0,0）。
        # 这里的0并不是以像素为单位，而是以行和列为单位，（0,0）即第一行第一列。最后的（3,0）意思是这个控件占三行,全部列
        grid.setSpacing(10)
        #向窗格添加窗口小部件，可以提供窗口小部件的行跨度和列跨度,使QLCDNumber小部件跨越4行。同时我们创建一个网格布局并在窗口小部件之间设置间距。
        print("2--->", grid.rowCount(), grid.columnCount())
        names = ['CLS',"BC","","CLOSE",
                 "7","8","9","/",
                 "4","5","6","*",
                 "1","2","3","-",
                 "0",".","=","+"]
        positions = [(i,j) for i in range(4,9) for j in range(4,8)]
        #创建了19个按钮并指定了具体的坐标位置,　这个列表生成式生成的列表类似一个矩阵，各元素的数值恰好是按钮在格栅布局中位置

        print(positions)
        for position, name in zip(positions,names):#这里使用的zip函数。python3中为了减少内存，zip函数返回的是一个对象。如果要展示列表，可通过 list() 转换。
            if name =="":
                continue
            button = QPushButton(name)
            grid.addWidget(button,*position)
            button.clicked.connect(self.Cli)
        #使用addWidget()方法创建并添加到布局中的按钮。同时当按下按钮的时候调用self.Cli()方法
        print("3--->", grid.rowCount(), grid.columnCount())
        self.show()

    def Cli(self):
        sender = self.sender().text()
        ls = ['/','*','-','=','+']
        if sender in ls:
            self.lcd.display("A")
        else:
            self.lcd.display(sender)

if __name__ =="__main__":
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())