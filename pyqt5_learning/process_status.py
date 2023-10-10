from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QLineEdit,QMessageBox,QProgressDialog
from PyQt5.QtCore import Qt
import sys,time

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("haha")
        self.resize(300,150)

        self.label = QLabel("file numbers",self)
        self.label.move(20,40)

        self.button = QPushButton("start", self)
        self.button.move(20,80)

        self.edit = QLineEdit("1000000", self)
        self.edit.move(100,40)

        self.show()

        self.button.clicked.connect(self.show_dialog)


    def show_dialog(self):        #新建了一个QProgressDialog对象progress，设置它的标题、标签、增加取消的按钮
        num = int(self.edit.text())
        progress = QProgressDialog(self)
        progress.setWindowTitle("pls wait...")
        progress.setLabelText("loading...")
        progress.setCancelButtonText("Cancel")
        progress.setMinimumDuration(1)
        #此属性保留对话框出现之前必须通过的时间
        #如果任务的预期持续时间小于minimumDuration，则对话框根本不会出现。这样可以防止弹出对话框，快速完成任务。
        # 对于预期超过minimumDuration的任务，对话框将在minimumDuration时间之后或任何进度设置后立即弹出。
        # 如果设置为0，则只要设置任何进度，将始终显示对话框。 默认值为4000毫秒,即4秒
        progress.setWindowModality(Qt.WindowModal)#此属性保留由模态小部件阻止的窗口
        progress.setRange(0,num)
        #使用setMinimum() 和setMaximum() 或构造函数来设置操作中的“steps”数量，
        # 并在操作进行时调用setValue()。setRange(0,num)就是设置其最小和最大值，这里最小值0，最大值num，num是根据输入框中的数字确定的。

        #progress.setValue(1000)
        for i in range(num):
            progress.setValue(i)
            if progress.wasCanceled():
                QMessageBox.warning(self,"Note:","Fail to load")
                break
        else:
            progress.setValue(num)
            #time.sleep(1)
            QMessageBox.information(self,"Note", "Load successful!")
        #setValue()该属性持有当前的进度。要使进度对话框按预期的方式工作，您应该首先将此属性设置为QProgressDialog的最小值， 您可以在中间调用setValue()任意次数。
        #过wasCanceled()判断我们是否按下取消按钮，如果按下则提示失败。若for循环顺利结束，执行else后的语句，表明成功。

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())