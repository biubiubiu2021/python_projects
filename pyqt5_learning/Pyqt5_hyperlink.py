from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel('<a href="http://www.intel.com">Intel</a>')
        label.setOpenExternalLinks(True)
        layout.addWidget(label)

        self.setLayout(layout)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()