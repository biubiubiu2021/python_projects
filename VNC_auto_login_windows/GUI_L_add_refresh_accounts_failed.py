import time
import win32gui
import pyautogui
import win32com.client
import win32con
import sys
import os
from PyQt5.QtWidgets import QApplication,QDialog, QDesktopWidget, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton, QButtonGroup, QScrollArea, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap
import getpass



# credentials = {
#     "amr\\666lab_raspdcg": "Teawithrabbit@345678",
#     "amr\\sys_paivauto": "Autoxpiv@1Autoxpiv@1",
#     ".\\general": "Passw0rd"
# }


# Define your users and passwords
username1 = "amr\\lab_raspdcg"
password1 = "Teawithrabbit@345678"

username2 = "amr\\sys_paivauto"
password2 = "Autoxpiv@1Autoxpiv@1"

username3 = ".\\general"
password3 = "Passw0rd"

# Create your dictionary dynamically
credentials = {
    username1: password1,
    username2: password2,
    username3: password3
}
credentials_updated = {}
print("original credential--->\n",credentials)


# Get the current username
username = getpass.getuser()

# Get the path to the user's home directory
user_folder = os.path.expanduser("~")

# Now you can continue to check for the file in the user's home directory
filename = "NUCwindows_account.txt"
file_path = os.path.join(user_folder, filename)

# Define your default information
default_info = f"""username1 = "{username1}"
password1 = "{password1}"

username2 = "{username2}"
password2 = "{password2}"

username3 = "{username3}"
password3 = "{password3}"
"""

# Check if the file doesn't exist or if it's empty
if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
    # If it doesn't exist or is empty, write the default info
    with open(file_path, 'w') as file:
        file.write(default_info)
else:
    # If the file exists and is not empty, check if it contains three users
    with open(file_path, 'r') as file:
        #contents_ALL = file.read()
        contents = file.readlines()
        print(file_path, filename)

        print("111content in txt:\n", contents)
        contents = [line for line in contents if line.strip() != ""]
        print("222content in txt:\n", contents)
    if len(contents) != 6:
        # Create QApplication
        app1 = QApplication(sys.argv)
        # If it doesn't contain three users, display a warning message
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Warning: The file does not contain three users.")
        msg.setWindowTitle("Warning")
        msg.exec_()
        # Execute QApplication
        sys.exit(app1.exec_())
    else:
        # Read the file and assign the values to the variables.
        # Check each line before accessing the list elements.
        print("content in txt:\n", contents)
        if isinstance(contents[0], str) and '"' in contents[0]:
            username11 = contents[0].split('"')[1]
            print("--->", username11)
        if isinstance(contents[1], str) and '"' in contents[1]:
            password11 = contents[1].split('"')[1]

        if isinstance(contents[2], str) and '"' in contents[2]:
            username22 = contents[2].split('"')[1]
        if isinstance(contents[3], str) and '"' in contents[3]:
            password22 = contents[3].split('"')[1]

        if isinstance(contents[4], str) and '"' in contents[4]:
            username33 = contents[4].split('"')[1]
        if isinstance(contents[5], str) and '"' in contents[5]:
            password33 = contents[5].split('"')[1]

        print("--->", username11)
        credentials_updated = {
            username11: password11,
            username22: password22,
            username33: password33
        }

        #credentials.update(credentials_updated)
        print("temp credential--->\n", credentials_updated)
        credentials = credentials_updated
        print("updated credential--->\n",credentials)
        username1 = username11
        password1 = password11

        username2 = username22
        password2 = password22

        username3 = username33
        password3 = password33




def enum_windows_callback(hwnd, vnc_windows):
    class_name = win32gui.GetClassName(hwnd)
    window_text = win32gui.GetWindowText(hwnd)
    #if "VNC Viewer" in window_text and not window_text.startswith("VNC Viewer") and ("(FL" in window_text or ("(SR" in window_text) or ("(zz" in window_text)):
    if "VNC Viewer" in window_text and not window_text.startswith("VNC Viewer") and ("(FL" in window_text or ("(fl" in window_text) or ("(SR" in window_text) or ("(sr" in window_text) or ("(ZZ" in window_text) or ("(zz" in window_text)):
        title_key = window_text.split(" -")[0].split(" (")[0]
        if title_key not in vnc_windows or ("(" not in vnc_windows[title_key][1] and hwnd > vnc_windows[title_key][0]) or "(" in window_text:
            vnc_windows[title_key] = (hwnd, window_text)

def click_center_of_window(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    time.sleep(0.1)
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(1)

    x, y, x1, y1 = win32gui.GetWindowRect(hwnd)
    center_x, center_y = (x + x1) // 2, (y + y1) // 2 +90
    pyautogui.click(center_x, center_y)


def login_to_windows_with_username(hwnd, username, password):
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    time.sleep(0.1)
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(1)
    pyautogui.typewrite(username)
    pyautogui.press('tab')
    pyautogui.typewrite(password)
    pyautogui.press('enter')

def login_to_windows_without_username(hwnd, password):
    #click_center_of_window(hwnd)
    time.sleep(0.5)
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    time.sleep(0.1)
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(1)
    pyautogui.typewrite(password)
    pyautogui.press('enter')

class VNCWindows(QWidget):
    def __init__(self, vnc_windows, window):
        super().__init__()
        self.layout = QVBoxLayout()
        self.layout.setSpacing(10)  # Set the spacing between widgets in the layout to 10 pixels
        self.setLayout(self.layout)
        self.window = window
        self.populate_layout(vnc_windows)

    def populate_layout(self, vnc_windows):

        for window_text, (hwnd, _) in vnc_windows.items():
            v_layout = QVBoxLayout()
            title_label = QLabel(window_text, self)
            v_layout.addWidget(title_label)
            h_layout = QHBoxLayout()
            h_layout.addLayout(v_layout)
            button = QPushButton("Unlock", self)
            button.clicked.connect(self.make_unlock_func(hwnd))
            button.setFixedWidth(100)
            h_layout.addWidget(button)
            self.layout.addLayout(h_layout)

    def make_unlock_func(self, hwnd):
        return lambda: self.unlock(hwnd)

    def unlock(self, hwnd):
        print("Unlock clicked!")
        #update the vnc list
        vnc_windows = {}
        win32gui.EnumWindows(enum_windows_callback, vnc_windows)
        vnc_exist_flag = 0
        vnc_handler =0
        try:
            for window_text, (hwnd_id, _) in vnc_windows.items():
                if hwnd == hwnd_id:
                    vnc_exist_flag =1
                    vnc_handler = hwnd_id
            if vnc_exist_flag:
                print("---> vnc exist!", "hwnd:", hwnd, "vnc_handler:", vnc_handler)
                vnc_exist_flag = 0
            else:
                print("---> vnc not alive","hwnd:", hwnd, "vnc_handler:", vnc_handler)
                sys.exit(1)

            #selected_username = "amr\\lab_raspdcg" if self.window.password_aaa.isChecked() else ("amr\\sys_paivauto" if self.window.password_bbb.isChecked() else ".\\general")
            selected_username = username1 if self.window.password_aaa.isChecked() else (username2 if self.window.password_bbb.isChecked() else username3)
            password = credentials[selected_username]
            status = "Yes" if self.window.status_yes.isChecked() else "No"
            print(f"Password: {password}, Status: {status}")
            if status == 'Yes':
                login_to_windows_without_username(hwnd, password)
            else:
                login_to_windows_with_username(hwnd, selected_username, password)
            time.sleep(2)
        except:
            msg_box = QMessageBox.critical(self, "Error!", "VNC not exist anymore, pls check!")

class Window(QWidget):
    def __init__(self, vnc_windows):
        super().__init__()
        self.setWindowTitle("Win_unlocker by_Caifu_v4.2")
        self.setGeometry(100, 100, 400, 400)

        # Center the window on the screen
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.vnc_windows = vnc_windows
        self.vnc_windows_widget = None
        self.refresh_button = None

        password_label = QLabel("Select the login account:", self)
        self.layout.addWidget(password_label)
        password_layout = QHBoxLayout()

        self.password_aaa = QRadioButton("Loading...", self)
        self.password_bbb = QRadioButton("Loading...", self)
        self.password_bbb.setChecked(True)
        self.password_ccc = QRadioButton("Loading...", self)

        password_layout.addWidget(self.password_aaa)
        password_layout.addWidget(self.password_bbb)
        password_layout.addWidget(self.password_ccc)
        self.layout.addLayout(password_layout)
        password_group = QButtonGroup(self)
        password_group.addButton(self.password_aaa)
        password_group.addButton(self.password_bbb)
        password_group.addButton(self.password_ccc)
        status_label = QLabel("Select the status: Yes for user locked, no for switch user", self)
        self.layout.addWidget(status_label)
        status_layout = QHBoxLayout()
        self.status_yes = QRadioButton("Yes", self)
        self.status_yes.setChecked(True)
        self.status_no = QRadioButton("No", self)
        status_layout.addWidget(self.status_yes)
        status_layout.addWidget(self.status_no)
        self.layout.addLayout(status_layout)
        status_group = QButtonGroup(self)
        status_group.addButton(self.status_yes)
        status_group.addButton(self.status_no)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFixedHeight(300)
        self.layout.addWidget(self.scroll_area)

        self.update_credentials()
        self.populate_layout()

    def update_credentials(self):
        # Define your users and passwords
        username1 = "amr\\lab_raspdcg"
        password1 = "Teawithrabbit@345678"

        username2 = "amr\\sys_paivauto"
        password2 = "Autoxpiv@1Autoxpiv@1"

        username3 = ".\\general"
        password3 = "Passw0rd"

        # Create your dictionary dynamically
        credentials = {
            username1: password1,
            username2: password2,
            username3: password3
        }
        credentials_updated = {}
        print("original credential--->\n", credentials)

        # Get the current username
        username = getpass.getuser()

        # Get the path to the user's home directory
        user_folder = os.path.expanduser("~")

        # Now you can continue to check for the file in the user's home directory
        filename = "NUCwindows_account.txt"
        file_path = os.path.join(user_folder, filename)

        # Define your default information
        default_info = f"""username1 = "{username1}"
        password1 = "{password1}"

        username2 = "{username2}"
        password2 = "{password2}"

        username3 = "{username3}"
        password3 = "{password3}"
        """

        # Check if the file doesn't exist or if it's empty
        if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
            # If it doesn't exist or is empty, write the default info
            with open(file_path, 'w') as file:
                file.write(default_info)
        else:
            # If the file exists and is not empty, check if it contains three users
            with open(file_path, 'r') as file:
                # contents_ALL = file.read()
                contents = file.readlines()
                print(file_path, filename)

                print("111content in txt:\n", contents)
                contents = [line for line in contents if line.strip() != ""]
                print("222content in txt:\n", contents)
            if len(contents) != 6:
                # Create QApplication
                app1 = QApplication(sys.argv)
                # If it doesn't contain three users, display a warning message
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Warning: The file does not contain three users.")
                msg.setWindowTitle("Warning")
                msg.exec_()
                # Execute QApplication
                sys.exit(app1.exec_())
            else:
                # Read the file and assign the values to the variables.
                # Check each line before accessing the list elements.
                print("content in txt:\n", contents)
                if isinstance(contents[0], str) and '"' in contents[0]:
                    username11 = contents[0].split('"')[1]
                    print("--->", username11)
                if isinstance(contents[1], str) and '"' in contents[1]:
                    password11 = contents[1].split('"')[1]

                if isinstance(contents[2], str) and '"' in contents[2]:
                    username22 = contents[2].split('"')[1]
                if isinstance(contents[3], str) and '"' in contents[3]:
                    password22 = contents[3].split('"')[1]

                if isinstance(contents[4], str) and '"' in contents[4]:
                    username33 = contents[4].split('"')[1]
                if isinstance(contents[5], str) and '"' in contents[5]:
                    password33 = contents[5].split('"')[1]

                print("--->", username11)
                credentials_updated = {
                    username11: password11,
                    username22: password22,
                    username33: password33
                }

                # credentials.update(credentials_updated)
                print("temp credential--->\n", credentials_updated)
                credentials = credentials_updated
                print("updated credential--->\n", credentials)
                username1 = username11
                password1 = password11

                username2 = username22
                password2 = password22

                username3 = username33
                password3 = password33
                print("username1", username1)

    def populate_layout(self):
        self.vnc_windows_widget = VNCWindows(self.vnc_windows, self)
        self.scroll_area.setWidget(self.vnc_windows_widget)

        self.layout.addStretch(1)

        self.button_layout = QHBoxLayout()
        self.layout.addLayout(self.button_layout)
        self.refresh_button = QPushButton("Refresh", self)
        self.refresh_button.clicked.connect(self.refresh)
        self.button_layout.addWidget(self.refresh_button)
        self.usage_button = QPushButton("Usage", self)
        self.usage_button.clicked.connect(self.show_usage_info)
        self.button_layout.addWidget(self.usage_button)

        total_width = 400  # Adjust this value as needed
        refresh_button_width = int(0.72 * total_width)  # 75% of total width
        usage_button_width = total_width - refresh_button_width  # 25% of total width

        self.refresh_button.setFixedWidth(refresh_button_width)
        self.usage_button.setFixedWidth(usage_button_width)

    def refresh(self):
        self.update_credentials()
        self.password_aaa.setText(self.username1)
        self.password_bbb.setText(self.username2)
        self.password_ccc.setText(self.username3)

        self.layout.removeWidget(self.vnc_windows_widget)
        self.vnc_windows_widget.deleteLater()
        self.vnc_windows_widget = None
        self.layout.removeWidget(self.refresh_button)
        self.refresh_button.deleteLater()
        self.refresh_button = None
        self.layout.removeItem(self.layout.itemAt(self.layout.count()-1))

        self.vnc_windows = {}
        win32gui.EnumWindows(enum_windows_callback, self.vnc_windows)

        self.populate_layout()

        self.update()
        self.repaint()



    def show_usage_info(self):
        # Create a QMessageBox
        msg_box = QMessageBox(self)

        # Set the title and text of the message box
        msg_box.setWindowTitle("Usage Information")
        msg_box.setText("1. Select which account you want to login (default: sys_paivauto)\n"
                        "2. Select weather the user has been locker (default: yes)\n"
                        "3. Select the VNC instance and click unlock\n"
                        "\n"
                        "Any questions, pls feel free to contact with Caifu 20231205")

        # Show the message box
        msg_box.exec_()


    def show_usage_info(self):
        # Create an ImageDialog
        dialog = ImageDialog(self)

        # Set the title of the dialog
        dialog.setWindowTitle("Usage Information")

        # Show the dialog
        dialog.exec_()

    def show_vnc_non_exist_warning(self):
        # Create a QMessageBox
        msg_box = QMessageBox(self)

        # Set the title and text of the message box
        msg_box.setWindowTitle("Usage Information")
        msg_box.setText("VNC not exist anymore, pls check!")


        # Show the message box
        msg_box.exec_()

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ImageDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create a QHBoxLayout for main layout
        main_layout = QHBoxLayout()


        # Find out whether we're running as a script or a frozen exe
        if getattr(sys, 'frozen', False):
            # If we're running as a frozen exe, the images are in the sys._MEIPASS directory
            image_dir = sys._MEIPASS
        else:
            # If we're running as a script, the images are in the current directory
            image_dir = os.path.dirname(os.path.abspath(__file__))

        # Load the images into QPixmaps
        pixmap1 = QPixmap(os.path.join(image_dir, 'usage5.png'))
        pixmap2 = QPixmap(os.path.join(image_dir, 'usage6.png'))
        pixmap3 = QPixmap(os.path.join(image_dir, 'usage7.png'))

        # # Load the images into QPixmaps
        # pixmap1 = QPixmap('usage5.png')
        # pixmap2 = QPixmap('usage6.png')
        # pixmap3 = QPixmap('usage7.png')

        # Create a QLabel for each image
        image_label1 = QLabel(self)
        image_label2 = QLabel(self)
        image_label3 = QLabel(self)

        # Create a QLabel for each text
        text_label1 = QLabel('UnlockWindows: Simply login', self)
        text_label2 = QLabel('SwitchUser-step1: Signout first', self)
        text_label3 = QLabel('SwitchUser-step2: Login', self)

        # Set the QPixmaps as the QLabel's pixmap
        image_label1.setPixmap(pixmap1)
        image_label2.setPixmap(pixmap2)
        image_label3.setPixmap(pixmap3)

        # Set the QLabel's style
        text_label1.setStyleSheet("color: green; font-weight: bold;")
        text_label2.setStyleSheet("color: green; font-weight: bold;")
        text_label3.setStyleSheet("color: green; font-weight: bold;")

        # Create a QVBoxLayout for each image-label pair
        layout1 = QVBoxLayout()
        layout1.addWidget(text_label1)
        layout1.addWidget(image_label1)

        layout2 = QVBoxLayout()
        layout2.addWidget(text_label2)
        layout2.addWidget(image_label2)

        layout3 = QVBoxLayout()
        layout3.addWidget(text_label3)
        layout3.addWidget(image_label3)

        # Add the QVBoxLayouts to the main QHBoxLayout
        main_layout.addLayout(layout1)
        main_layout.addLayout(layout2)
        main_layout.addLayout(layout3)

        # Set the main layout on the QDialog
        self.setLayout(main_layout)

vnc_windows = {}
win32gui.EnumWindows(enum_windows_callback, vnc_windows)
print("vnc windows list --->", vnc_windows)
app = QApplication([])
window = Window(vnc_windows)
window.show()
sys.exit(app.exec_())