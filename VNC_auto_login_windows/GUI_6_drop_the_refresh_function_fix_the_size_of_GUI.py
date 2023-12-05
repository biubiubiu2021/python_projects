import time
import win32gui
import pyautogui
import win32com.client
import win32con
import sys
import io
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton, QButtonGroup
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

credentials = [
    ("amr\lab_raspdcg", "Teawithrabbit@345678"),
    ("amr\sys_paivauto", "Autoxpiv@1Autoxpiv@1"),
]

def enum_windows_callback(hwnd, vnc_windows):
    class_name = win32gui.GetClassName(hwnd)
    window_text = win32gui.GetWindowText(hwnd)
    if "VNC Viewer" in window_text and not window_text.startswith("VNC Viewer"):
        title_key = window_text.split(" -")[0].split(" (")[0]
        if title_key not in vnc_windows or ("(" not in vnc_windows[title_key][1] and hwnd > vnc_windows[title_key][0]) or "(" in window_text:
            vnc_windows[title_key] = (hwnd, window_text)

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
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    time.sleep(0.1)
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(1)
    pyautogui.typewrite(password)
    pyautogui.press('enter')


def take_screenshot(hwnd, window_text):
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
    time.sleep(0.5)
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    time.sleep(0.5)
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    time.sleep(1)
    win32gui.SetForegroundWindow(hwnd)
    x, y, x1, y1 = win32gui.GetWindowRect(hwnd)
    center_x, center_y = (x + x1) // 2, (y + y1) // 2
    pyautogui.click(center_x, center_y)
    time.sleep(0.5)
    img = pyautogui.screenshot(region=(center_x - 200, center_y - 10, 400, 150))
    bio = io.BytesIO()
    img.save(bio, format='PNG')
    pixmap = QPixmap()
    pixmap.loadFromData(bio.getvalue(), 'PNG')
    pixmap = pixmap.scaled(300, 100, Qt.KeepAspectRatio)
    return pixmap

class Window(QWidget):
    def __init__(self, vnc_windows):
        super().__init__()
        self.setWindowTitle("VNC Unlocker")
        self.setGeometry(100, 100, 400, 600)
        layout = QVBoxLayout()

        password_label = QLabel("Select the login account:", self)
        layout.addWidget(password_label)
        password_layout = QHBoxLayout()
        self.password_aaa = QRadioButton("amr\lab_raspdcg", self)
        self.password_bbb = QRadioButton("amr\sys_paivauto", self)
        self.password_bbb.setChecked(True)
        password_layout.addWidget(self.password_aaa)
        password_layout.addWidget(self.password_bbb)
        layout.addLayout(password_layout)
        password_group = QButtonGroup(self)
        password_group.addButton(self.password_aaa)
        password_group.addButton(self.password_bbb)
        status_label = QLabel("Select the status: Yes for user locked, no for user empty", self)
        layout.addWidget(status_label)
        status_layout = QHBoxLayout()
        self.status_yes = QRadioButton("Yes", self)
        self.status_yes.setChecked(True)
        self.status_no = QRadioButton("No", self)
        status_layout.addWidget(self.status_yes)
        status_layout.addWidget(self.status_no)
        layout.addLayout(status_layout)
        status_group = QButtonGroup(self)
        status_group.addButton(self.status_yes)
        status_group.addButton(self.status_no)

        for window_text, (hwnd, _) in vnc_windows.items():
            pixmap = take_screenshot(hwnd, window_text)
            pixmap = pixmap.scaled(300, 100, Qt.KeepAspectRatio)
            v_layout = QVBoxLayout()
            title_label = QLabel(window_text, self)
            v_layout.addWidget(title_label)
            image_label = QLabel(self)
            image_label.setPixmap(pixmap)
            v_layout.addWidget(image_label)
            h_layout = QHBoxLayout()
            h_layout.addLayout(v_layout)
            button = QPushButton("Unlock", self)
            button.clicked.connect(self.make_unlock_func(hwnd))
            button.setFixedWidth(80)
            h_layout.addWidget(button)
            layout.addLayout(h_layout)

        layout.addStretch(1)  # Add a stretch to the layout

        self.setLayout(layout)

    def make_unlock_func(self, hwnd):
        return lambda: self.unlock(hwnd)
    def unlock(self, hwnd):
        print("Unlock clicked!")
        password = "Teawithrabbit@345678" if self.password_aaa.isChecked() else "Autoxpiv@1Autoxpiv@1"
        status = "Yes" if self.status_yes.isChecked() else "No"
        print(f"Password: {password}, Status: {status}")
        if status == 'Yes':
            login_to_windows_without_username(hwnd, password)
        else:
            if password == "Teawithrabbit@345678":
                selected_username = "amr\lab_raspdcg"
            elif password == "Autoxpiv@1Autoxpiv@1":
                selected_username = "amr\sys_paivauto"
            login_to_windows_with_username(hwnd, selected_username, password)
        time.sleep(2)



vnc_windows = {}
win32gui.EnumWindows(enum_windows_callback, vnc_windows)
app = QApplication([])
window = Window(vnc_windows)
window.show()
sys.exit(app.exec_())