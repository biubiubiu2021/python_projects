from PyQt5.QtWidgets import QApplication, QMainWindow,QAction,qApp,QMenu
from PyQt5.QtGui import QIcon
import sys

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('准备就绪！')
        #调用QWidget.QMainWindow类的statusBar()方法。 该方法的第一个调用创建一个状态栏。 后续调用返回状态栏对象。 showMessage()在状态栏上显示一条消息。
        self.setGeometry(300,300,400,300)
        self.setWindowTitle("hahaha")

        exitAct = QAction(QIcon('exit.png'),"Exit(&E)",self)#QAction是使用菜单栏，工具栏或自定义键盘快捷方式执行操作的抽象。
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip("Exit program")
        #在上述三行中，我们创建一个具有特定图标和“退出”标签的动作。此外，为此操作定义了快捷方式。当我们将鼠标指针悬停在菜单项上时，第三行创建状态栏显示在状态栏中。
        exitAct.triggered.connect(qApp.quit)
        #当我们选择这个特定的动作时，发出触发信号。 信号连接到QApplication小部件的quit()方法。 这终止了应用程序


        #我们有三个菜单项： 其中两个位于文件菜单中（新建、退出），另一个位于文件的保存子菜单中。
        saveMenu = QMenu("save (&s)",self)#使用QMenu创建新子菜单,

        saveAct = QAction(QIcon('save.png'),'Save',self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip("Saving files")

        saveasAct = QAction(QIcon('saveas.png'),'Save as',self)
        saveasAct.setShortcut('Ctrl+P')
        saveasAct.setStatusTip("Saving files as")

        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveasAct)
        #两个动作使用addAction()被添加到子菜单中。

        newAct = QAction(QIcon('new.png'),"Create(&N)", self)
        newAct.setShortcut('Ctrl+N')
        newAct.setStatusTip('新建文件')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("Files(&F)")
        virwMenu = menubar.addMenu("View(&V)")
        aboutMenu = menubar.addMenu("About(&A)")
        #menuBar()方法创建一个菜单栏。 我们使用addMenu()创建文件菜单，并使用addAction()添加操作。
        #在退出、文件后面都增加了“&”这个符号，增加这个符号后，当我们按住“Alt+F”的时候就能快速打开文件这个菜单，同理按住“Alt+E”的时候就能退出了

        fileMenu.addAction(newAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        #工具栏
        #各项命令都是在菜单栏当中，但是我们可以把一些常用的命令放在工具栏上，例如新建、打开、保存等等。
        toolBar = self.addToolBar("tools")
        toolBar.addAction(newAct)
        toolBar.addAction(saveAct)
        toolBar.addAction(saveasAct)
        toolBar.addAction(exitAct)

        self.show()

    #Windows操作系统中任何地方右击鼠标会出现俗称的“右键菜单”，其实就是指上下文菜单。
    def contextMenuEvent(self,event): #这个函数名是定死的，不能改！这里是重写原来的函数方法，
        #要使用上下文菜单，我们必须重新实现contextMenuEvent()方法。
        contentMenu = QMenu(self)

        newAct = contentMenu.addAction("New")
        saveAct = contentMenu.addAction("save")
        quitAct = contentMenu.addAction("exit")
        action = contentMenu.exec_(self.mapToGlobal(event.pos()))
        #使用exec_()方法显示上下文菜单。 从事件对象获取鼠标指针的坐标。 mapToGlobal()方法将窗口小部件坐标转换为全局屏幕坐标。
        if action == quitAct:
            qApp.quit()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())