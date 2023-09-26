import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication,QLabel

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,350,250)
        self.setWindowTitle("pyqt5")

        self.lab=QLabel("direction", self)
        self.lab.setGeometry(150,100,50,50)

        self.letter=QLabel("Letters", self)
        self.letter.setGeometry(100,50,50,50)

        self.show()

    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Up:
            self.lab.setText('⬆')
        elif e.key() == Qt.Key_Down:
            self.lab.setText('⬇')
        elif e.key() == Qt.Key_Left:
            self.lab.setText('⬅')
        else:
            self.lab.setText('➡')
        if e.key() == Qt.Key_A:
            self.letter.setText("AAAAAAAAAAAAA")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())