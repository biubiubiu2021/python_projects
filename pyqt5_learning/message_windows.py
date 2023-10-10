from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QCheckBox
#QMessageBox类提供了一个模态对话框，用于通知用户或询问用户问题并接收答案。
#消息框显示主要文本以提醒用户情况，信息性文本以进一步解释警报或询问用户一个问题，以及可选的详细文本，以便在用户请求时提供更多数据。 消息框还可以显示用于接受用户响应的图标和标准按钮。
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,330,300)
        self.setWindowTitle("haha")

        self.label = QLabel("display the single info",self)
        self.label.setFixedWidth(200)
        self.label.move(20,20)
        self.bt1 = QPushButton('提示',self)
        self.bt1.move(20,70)
        self.bt2 = QPushButton('询问',self)
        self.bt2.move(120,70)
        self.bt3 = QPushButton('警告',self)
        self.bt3.move(220,70)
        self.bt4 = QPushButton('错误',self)
        self.bt4.move(20,140)
        self.bt5 = QPushButton('关于',self)
        self.bt5.move(120,140)
        self.bt6 = QPushButton('关于Qt',self)
        self.bt6.move(220,140)

        self.bt1.clicked.connect(self.info)
        self.bt2.clicked.connect(self.question)
        self.bt3.clicked.connect(self.warning)
        self.bt4.clicked.connect(self.critical)
        self.bt5.clicked.connect(self.about)
        self.bt6.clicked.connect(self.aboutQt)
        #，消息对话框分为五种，分别是提示信息、询问、警告、错误、关于，其中关于又分为两种，一种是一般性关于、另一种是关于Qt的介绍
        self.show()

    def info(self):
        reply = QMessageBox.information(self,"note:", "This is a Note dialog", QMessageBox.Ok| QMessageBox.Close, QMessageBox.Close)
        #信息对话框调用格式：
        #QMessageBox.information(QWidget, str, str, buttons: Union[QMessageBox.StandardButtons, QMessageBox.StandardButton] = QMessageBox.Ok, defaultButton: QMessageBox.StandardButton = MessageBox.NoButton)
        #标题和文本的信息消息对话框。这句话分别对应了第一、二、三个参数
        #第四个参数则是我们要在消息对话框上想要显示的按钮。
        #第五个参数defaultButton指定按Enter键时使用的按钮。如果defaultButton是QMessageBox.NoButton，QMessageBox会自动选择合适的默认值。
        if reply == QMessageBox.Ok:
            self.label.setText("You select OK!")
        else:
            self.label.setText("You select Close!")

    def question(self):
        reply = QMessageBox.question(self,"question:","This is a question dialog, default answer is NO", QMessageBox.Yes | QMessageBox.No |QMessageBox.Cancel, QMessageBox.No)
        #询问对话框
        if reply == QMessageBox.Yes:
            self.label.setText("You choose Yes!")
        elif reply == QMessageBox.No:
            self.label.setText("You choose No!")
        elif reply == QMessageBox.Cancel:
            self.label.setText("You choose Cancel!")

    def warning(self):
        #reply = QMessageBox.warning(self,"Warning", "This is a warning message dialog", QMessageBox.Save|QMessageBox.Discard|QMessageBox.Cancel, QMessageBox.Save)
        #上面是静态函数的方式

        #下面是基于属性的方法

        #在对话框中增加一个复选框
        cb = QCheckBox("do for all docs")
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Warning!")#设置消息对话框的标题：警告。
        msgBox.setIcon(QMessageBox.Warning)#设置消息对话框的图标：QMessageBox.Warning，也就是警告图标，当然也可以选择QMessageBox.Information、QMessageBox.Question、QMessageBox.Critical
        msgBox.setText("This is a warning dialog")#设置消息对话框的要显示的消息框文本，如果文本格式设置（QMessageBox.textFormat），文本将被解释为纯文本或富文本。 默认设置为Qt.AutoText，即消息框将尝试自动检测文本的格式
        msgBox.setInformativeText("save the changes?")#设置消息对话框更完整描述的信息性文本，可以使用Infromative文本来扩展text()以向用户提供更多信息。

        Save = msgBox.addButton("Save", QMessageBox.AcceptRole)
        NoSave = msgBox.addButton("Cancel", QMessageBox.ResetRole)
        Cancel = msgBox.addButton("Discard", QMessageBox.DestructiveRole)#新建了三个按钮
        msgBox.setDefaultButton(Save)

        msgBox.setCheckBox(cb)
        cb.stateChanged.connect(self.check)
        #在消息对话框上设置之前建立的那个复选框。当我们选择这个复选框的时候产生了stateChanged信号，对应的将连接check()这个槽函数

        reply = msgBox.exec()#让消息对话框能够显示出来，并将我们选中的按钮返回给reply这个变量

        #选择不同的按钮时候，我们则在标签上有不同的显示。
        if reply == QMessageBox.AcceptRole: #AcceptRole表示点击按钮可以接受对话框
            self.label.setText("you choose to save!")
        elif reply == QMessageBox.RejectRole:#RejectRole表示单击该按钮将导致对话框被拒绝
            self.label.setText("you choose to Cancel!")
        else:#DestructiveRole表示单击该按钮将导致破坏性更改（例如“丢弃更改”）并关闭对话框
            self.label.setText("You choose to discard!")

    def check(self):
        if self.sender().isChecked():#self.sender()就是传递信号过来的对象，这里就是复选框
            #isChecked()返回的是一个布尔值，也就是判断是否被选中，选中了就显示打勾，否则就是不打勾。
            self.label.setText("double check you choose Yes")
        else:
            self.label.setText("double check you choose NO")

    def critical(self):
        #reply = QMessageBox.critical(self, "Error", "This is a Error dialog", QMessageBox.Retry|QMessageBox.Abort|QMessageBox.Ignore, QMessageBox.Retry)
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Warning!")
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("This is a error info dialog")
        msgBox.setStandardButtons(QMessageBox.Retry| QMessageBox.Abort |QMessageBox.Ignore)#表明消息对话框中使用哪些标准按钮。
        #该属性保存要在详细信息区域中显示的文本。文本将被解释为纯文本。默认情况下，此属性包含一个空字符串。
        msgBox.setDefaultButton(QMessageBox.Retry)
        msgBox.setDetailedText("this is the detail info")
        reply = msgBox.exec()
        if reply == QMessageBox.Retry:
            self.label.setText("you choose to retry!")
        elif reply == QMessageBox.Abort:
            self.label.setText("you choose to Abort!")
        else:
            self.label.setText("You choose to ignore!")

    def about(self):
        #QMessageBox.about(self,"about", "this is a message dialog") #这是静态函数方法，下面是基于属性的方法
        msgBox = QMessageBox(QMessageBox.NoIcon,"about", "66666666")
        #建立了QMessageBox对象，一开始的时候就将标题还有要显示的内容带入了，同时还表明这是一个没有图标的消息对话框。
        msgBox.setIconPixmap(QPixmap("./1.ico"))
        #对图标进行了设计，使用setIconPixmap()函数，注意参数必须是QPixmap类型的。
        msgBox.exec()

    def aboutQt(self):
        QMessageBox.aboutQt(self,"about Qt")



if __name__ =="__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())