import time
import win32gui
import pyautogui
import win32com.client
import win32con
import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton, QButtonGroup, QScrollArea, QMessageBox
from PyQt5.QtCore import Qt

credentials = {
    "amr\\lab_raspdcg": "Teawithrabbit@345678",
    "amr\\sys_paivauto": "Autoxpiv@1Autoxpiv@1",
    ".\\general": "Passw0rd"
}

def enum_windows_callback(hwnd, vnc_windows):
    class_name = win32gui.GetClassName(hwnd)
    window_text = win32gui.GetWindowText(hwnd)
    if "VNC Viewer" in window_text and not window_text.startswith("VNC Viewer") and ("FL" in window_text or ("SR" in window_text) or ("zz" in window_text)):
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
            button.setFixedWidth(80)
            h_layout.addWidget(button)

            signout_button = QPushButton("Signout", self)
            signout_button.clicked.connect(self.make_signout_func(hwnd))
            signout_button.setFixedWidth(80)
            h_layout.addWidget(signout_button)

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

            selected_username = "amr\\lab_raspdcg" if self.window.password_aaa.isChecked() else ("amr\\sys_paivauto" if self.window.password_bbb.isChecked() else ".\\general")
            password = credentials[selected_username]
            status = "Yes" if self.window.status_yes.isChecked() else "No"
            print(f"Password: {password}, Status: {status}")
            if status == 'Yes':
                login_to_windows_without_username(hwnd, password)
            else:
                login_to_windows_with_username(hwnd, selected_username, password)
            time.sleep(2)
        except:
            msg_box = QMessageBox.critical(self, "Error!", "VNC not exist anymore, pls refresh!")


    def make_signout_func(self, hwnd):
        return lambda: self.signout(hwnd)

    def signout(self, hwnd):
        print("---> signout clicked")
        #update the vnc list
        vnc_windows = {}
        win32gui.EnumWindows(enum_windows_callback, vnc_windows)
        vnc_exist_flag = 0
        vnc_handler =0
        # Set the focus to the specified window
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


            win32gui.SetForegroundWindow(hwnd)

            # Wait for the window to gain focus
            time.sleep(1)

            # Press the keys to switch account.
            pyautogui.hotkey('ctrl', 'alt', 'del')
            time.sleep(1)
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)

            # Click the 'Other user' button. You may need to adjust the coordinates.
            # You might need to find the exact location of the 'Other user' button on your screen.
            # This can be done using the 'pyautogui.position()' function in a Python terminal,
            # which will give you the current position of the mouse.
            # pyautogui.click(x=100, y=200)  # Replace with the actual coordinates of the 'Other user' button

            # Locate the 'Other user' button based on an image file
            time.sleep(3)
            location = pyautogui.locateOnScreen('other_user_button.png', confidence=0.8)

            # Click the 'Other user' button
            if location:
                print("---> find the location")
                pyautogui.click(location)

            else:
                print("---> retry:")
                time.sleep(3)
                location = pyautogui.locateOnScreen('other_user_button.png', confidence=0.9)
            # Type the username and password of the other account

            self.window.status_no.setChecked(True)

            # Get the screen coordinates of the top-left corner of your GUI window
            gui_x = self.window.frameGeometry().x()
            gui_y = self.window.frameGeometry().y()

            # Get the width and height of your GUI window
            gui_width = self.window.frameGeometry().width()
            gui_height = self.window.frameGeometry().height()

            # Calculate the coordinates of the center of your GUI window
            center_x = gui_x + gui_width // 2
            center_y = gui_y + gui_height // 2

            # Move the mouse to the center of the GUI window
            pyautogui.moveTo(center_x, center_y)
        except:
            msg_box = QMessageBox.critical(self, "Error!", "VNC not exist anymore, pls refresh!")


class Window(QWidget):
    def __init__(self, vnc_windows):
        super().__init__()
        self.setWindowTitle("Win_unlocker by_Caifu_v4.0")
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
        self.password_aaa = QRadioButton("amr\\lab_raspdcg", self)
        self.password_bbb = QRadioButton("amr\\sys_paivauto", self)
        self.password_bbb.setChecked(True)
        self.password_ccc = QRadioButton(".\\general", self)
        password_layout.addWidget(self.password_aaa)
        password_layout.addWidget(self.password_bbb)
        password_layout.addWidget(self.password_ccc)
        self.layout.addLayout(password_layout)
        password_group = QButtonGroup(self)
        password_group.addButton(self.password_aaa)
        password_group.addButton(self.password_bbb)
        password_group.addButton(self.password_ccc)
        status_label = QLabel("Select the status: Yes for user locked, no for user empty", self)
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

        self.populate_layout()

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

        # After refreshing, set status_yes to True
        self.status_yes.setChecked(True)

    def show_usage_info(self):
        # Create a QMessageBox
        msg_box = QMessageBox(self)

        # Set the title and text of the message box
        msg_box.setWindowTitle("Usage Information")
        msg_box.setText("1. Select which account you want to login (default: sys_paivauto)\n"
                        "2. Select weather the user has been locker (default: yes)\n"
                        "3. Select the VNC instance and click unlock\n"
                        "4. If unlock failed, retry more times (network performance limited)\n"
                        "5. If new open or close VNC, click refresh\n"
                        "\n"
                        "Any questions, pls feel free to contact with Caifu 20231205")

        # Show the message box
        msg_box.exec_()

    def show_vnc_non_exist_warning(self):
        # Create a QMessageBox
        msg_box = QMessageBox(self)

        # Set the title and text of the message box
        msg_box.setWindowTitle("Usage Information")
        msg_box.setText("VNC not exist anymore, pls Refresh!")

        # Show the message box
        msg_box.exec_()



vnc_windows = {}
win32gui.EnumWindows(enum_windows_callback, vnc_windows)
app = QApplication([])
window = Window(vnc_windows)
window.show()
sys.exit(app.exec_())