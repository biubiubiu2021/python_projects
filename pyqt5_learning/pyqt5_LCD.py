import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QLCDNumber,QDial,QApplication,QSlider

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,350,350) #主页面窗口大小
        self.setWindowTitle("pyqt5")

        #lcd = QLCDNumber() #没有这个self, LCD 不会价值到这个窗口上
        self.lcd = QLCDNumber(self) #创建一个LCD显示
        dial = QDial(self)#增加一个转盘
        slider = QSlider(self)#创建一个滑条

        self.lcd.setGeometry(100,50,150,60)
        dial.setGeometry(120,120,100,100)
        slider.setGeometry(120,250,200,30)
        slider.setOrientation(Qt.Horizontal)#设置滑条方向

        dial.valueChanged.connect(self.lcd.display) #将QDial这个小部件的一个valueChanged信号连接到lcd数字的显示槽
        slider.valueChanged.connect(self.lcd.display)

        self.show()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())