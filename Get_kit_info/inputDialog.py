from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QInputDialog,QTextBrowser
import sys
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500,500,500,500)
        self.setWindowTitle("haha")

        self.label1 = QLabel("Name:", self)
        self.label1.move(20,20)

        self.label2 = QLabel("Age:", self)
        self.label2.move(20,80)

        self.label3 = QLabel("Sex:", self)
        self.label3.move(20,140)

        self.label4 = QLabel("Height(cm):", self)
        self.label4.move(20,200)

        self.label5 = QLabel("Info:", self)
        self.label5.move(20,260)

        self.label6 = QLabel("HAHA", self)
        self.label6.move(80,20)

        self.label7 = QLabel("30", self)
        self.label7.move(80, 80)

        self.label8 = QLabel("Male", self)
        self.label8.move(80, 140)

        self.label9 = QLabel("160", self)
        self.label9.move(80, 200)

        self.label10 = QLabel("NA", self)
        self.label10.move(80, 260)

        self.bt1 = QPushButton("Edit Name", self)
        self.bt1.move(200, 20)

        self.bt2 = QPushButton("Edit Age", self)
        self.bt2.move(200, 80)

        self.bt3 = QPushButton("Edit sex", self)
        self.bt3.move(200, 140)

        self.bt4 = QPushButton("Edit Height", self)
        self.bt4.move(200, 200)

        self.bt5 = QPushButton("Edit Info", self)
        self.bt5.move(200, 260)

        self.bt1.clicked.connect(self.show_dialog)
        self.bt2.clicked.connect(self.show_dialog)
        self.bt3.clicked.connect(self.show_dialog)
        self.bt4.clicked.connect(self.show_dialog)
        self.bt5.clicked.connect(self.show_dialog)
        self.show()

    def show_dialog(self):
        sender = self.sender()
        sex = ['Male','Female']
        print("---->",sender)
        if sender == self.bt1:
            text, ok = QInputDialog.getText(self,"Edit Name","Pls input the name:")
            #按下按钮1，此时显示输入对话框。 第一个字符串是一个对话标题，第二个是对话框中的一个消息。 对话框返回输入的文本和布尔值。 如果我们点击Ok按钮，布尔值为true。
            if ok:
                self.label6.setText(text)
                #按下ok键，则标签6的text值是从对话框接收的文本
        elif sender == self.bt2:
            text, ok = QInputDialog.getInt(self,"Edit Age", "Pls input the new age:",min=1)
            #以输入整数，最小值、最大值可以自己设定，步长也可以自己设定
            if ok:
                self.label7.setText(str(text))
        elif sender == self.bt3:
            text, ok = QInputDialog.getItem(self,"Edit Sex", "Pls input the new sex:", sex)
            # 可以输入选择项，待选放到列表中，这里的列表就是sex
            if ok:
                self.label8.setText(text)
        elif sender == self.bt4:
            text, ok = QInputDialog.getDouble(self,"Edit Height", "Pls input the new heoght:", min=1.0)
            #可以输入浮点型小数，最小值、最大值可以自己设定
            if ok:
                self.label9.setText(str(text))
        elif sender == self.bt5:
            text, ok = QInputDialog.getMultiLineText(self,"Edit Info", "Pls input the new Info:")
            #可以输入富文本，在里面增加一些格式信息
            if ok:
                self.label10.setText(text)


if __name__ =='__main__':
    app=QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())