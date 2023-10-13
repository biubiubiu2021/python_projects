import sys
from PyQt5.QtWidgets import QApplication,QLabel,QWidget
from PyQt5.QtGui import QPainter,QColor,QPen
from PyQt5.QtCore import Qt

class Example(QWidget):
    distance_from_center = 0
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)#鼠标坐标（x,y）的获取,启用鼠标跟踪，即使没有按钮被按下，小部件也会接收鼠标移动事件

    def initUI(self):
        self.setGeometry(200,200,1000,500)
        self.setWindowTitle("pyqt5 plant")
        self.label = QLabel(self)
        self.label.resize(500,40)
        self.show()
        self.pos = None

    def mouseMoveEvent(self, event):
        distance_from_center = round(((event.y() - 250)**2 +(event.x()-500)**2)**0.5)#计算鼠标坐标与中心点的距离（运用勾股定理进行计算）
        self.label.setText('Coordinate:(x: %d, y: %d)'%(event.x(),event.y()) + "distance to center: " + str(distance_from_center))
        self.pos = event.pos()
        self.update()#捕捉鼠标移动事件,把得到的坐标已经一些相关的信息显示在label上。必须调用函数update()才能更新图形。

    def paintEvent(self,event):

        if self.pos:
            q = QPainter(self)
            q.drawLine(0,0,self.pos.x(),self.pos.y())
            self.update()

            #绘制一条线，这条线的起点坐标在（0,0），另外一个端点随鼠标移动而移动

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

     #event参数是QMouseEvent对象，存储事件的其他信息。常用方法有：
# x() 和 y()：返回相对于控件空间的鼠标坐标值；
# pos()： 返回相对于控件空间的QPoint对象；
# localPos()：返回相对于控件空间的QPointF对象；
# globalX() 和 globalY(): 返回相对于屏幕的x,y 坐标值；
# globalPos(): 返回相对于屏幕的QPoint对象；
# windowPos(): 返回相对于窗口的QPointF对象；
# screenPos() : 返回相对于屏幕的QPointF对象；
# button(): 返回以下枚举值（只列举了部分），用以判断是哪个鼠标键触发了事件；
# Qt.NoButton (0): 没有按下鼠标键。例如移动鼠标时的button()返回值；
# Qt.LeftButton (1): 按下鼠标左键；
# Qt.RightButton (2): 按下鼠标右键；
# t.Mion 或 Qt.MiddleButton (4): 按下鼠标中键。
# buttons(): 返回前面所列枚举值的组合，用于判断同时按下了哪些键；
# modifiers(): 判断按下了哪些修饰键（Shift,Ctrl , Alt,等等）；
# timestamp() : 返回事件发生的时间。
# ————————————————
# 版权声明：本文为CSDN博主「seniorwizard」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/seniorwizard/article/details/110824308