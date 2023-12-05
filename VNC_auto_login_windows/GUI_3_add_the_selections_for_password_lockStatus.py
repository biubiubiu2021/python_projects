import time
import win32gui
import pyautogui
import win32com.client
import win32con
import sys
import io
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton, QButtonGroup


from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

credentials = [
    ("amr\lab_raspdcg", "Teawithrabbit@345678"),
    ("amr\sys_paivauto", "Autoxpiv@1Autoxpiv@1"),
    # Add more as needed
]


# Callback function to retrieve VNC Viewer windows
def enum_windows_callback(hwnd, vnc_windows):
    class_name = win32gui.GetClassName(hwnd)
    window_text = win32gui.GetWindowText(hwnd)
    if "VNC Viewer" in window_text and not window_text.startswith("VNC Viewer"):
        # Consider only the part of the title before the first space followed by a hyphen or parenthesis
        title_key = window_text.split(" -")[0].split(" (")[0]
        # If the title_key is not in the dictionary, or the current hwnd is larger and the existing title does not have parentheses, or the current title has parentheses, add/update it
        if title_key not in vnc_windows or (
                "(" not in vnc_windows[title_key][1] and hwnd > vnc_windows[title_key][0]) or "(" in window_text:
            vnc_windows[title_key] = (hwnd, window_text)


def take_screenshot(hwnd, window_text):
    # Minimize and then restore the window
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
    time.sleep(0.5)  # Wait for a bit to let the window minimize
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    time.sleep(0.5)  # Wait for a bit to let the window restore

    # Use the Alt key to bring the window to the foreground
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')

    # Sleep for a bit to let the window come to the foreground
    time.sleep(1)

    # Set the window to the foreground
    win32gui.SetForegroundWindow(hwnd)
    x, y, x1, y1 = win32gui.GetWindowRect(hwnd)

    # Calculate the center coordinates
    center_x, center_y = (x + x1) // 2, (y + y1) // 2

    # Click inside the window to activate it
    pyautogui.click(center_x, center_y)
    time.sleep(0.5)  # Wait for a bit to let the window update

    # Capture a 200x200 region around the center
    img = pyautogui.screenshot(region=(center_x - 200, center_y - 10, 400, 150))

    # Save the image to a BytesIO object
    bio = io.BytesIO()
    img.save(bio, format='PNG')

    # Load the image into a QPixmap
    pixmap = QPixmap()
    pixmap.loadFromData(bio.getvalue(), 'PNG')

    # Resize the QPixmap
    pixmap = pixmap.scaled(300, 100, Qt.KeepAspectRatio)

    return pixmap

class Window(QWidget):
    def __init__(self, vnc_windows):
        super().__init__()

        self.setWindowTitle("VNC Unlocker")
        self.setGeometry(100, 100, 400, 600)

        layout = QVBoxLayout()

        # Add password selection label and radio buttons
        password_label = QLabel("Select the login account:", self)
        layout.addWidget(password_label)

        password_layout = QHBoxLayout()
        self.password_aaa = QRadioButton("amr\lab_raspdcg", self)
        self.password_aaa.setChecked(True)  # Default selection
        self.password_bbb = QRadioButton("amr\sys_paivauto", self)
        password_layout.addWidget(self.password_aaa)
        password_layout.addWidget(self.password_bbb)
        layout.addLayout(password_layout)

        # Group password radio buttons
        password_group = QButtonGroup(self)
        password_group.addButton(self.password_aaa)
        password_group.addButton(self.password_bbb)

        # Add status selection label and radio buttons
        status_label = QLabel("Select the status: Yes for user locked, no for user empty", self)
        layout.addWidget(status_label)

        status_layout = QHBoxLayout()
        self.status_yes = QRadioButton("Yes", self)
        self.status_yes.setChecked(True)  # Default selection
        self.status_no = QRadioButton("No", self)
        status_layout.addWidget(self.status_yes)
        status_layout.addWidget(self.status_no)
        layout.addLayout(status_layout)

        # Group status radio buttons
        status_group = QButtonGroup(self)
        status_group.addButton(self.status_yes)
        status_group.addButton(self.status_no)

        for window_text, (hwnd, _) in vnc_windows.items():
            # Take a screenshot and get the QPixmap
            pixmap = take_screenshot(hwnd, window_text)
            pixmap = pixmap.scaled(300, 100, Qt.KeepAspectRatio)

            # Create a vertical layout for the title and image
            v_layout = QVBoxLayout()

            # Create a label with the window title
            title_label = QLabel(window_text, self)
            v_layout.addWidget(title_label)

            # Create a label with the image
            image_label = QLabel(self)
            image_label.setPixmap(pixmap)
            v_layout.addWidget(image_label)

            # Create a horizontal layout for the vertical layout and button
            h_layout = QHBoxLayout()

            # Add the vertical layout and button to the horizontal layout
            h_layout.addLayout(v_layout)

            # Create a button
            button = QPushButton("Unlock", self)
            button.clicked.connect(self.unlock)
            button.setFixedWidth(40)  # Set the width of the button
            h_layout.addWidget(button)

            # Add the horizontal layout to the main layout
            layout.addLayout(h_layout)

        self.setLayout(layout)

    def unlock(self):
        print("Unlock clicked!")
        password = "Teawithrabbit@345678" if self.password_aaa.isChecked() else "Autoxpiv@1Autoxpiv@1"
        status = "Yes" if self.status_yes.isChecked() else "No"
        print(f"Password: {password}, Status: {status}")




# Dictionary to store VNC Viewer windows
vnc_windows = {}

# Enumerate all top-level windows
win32gui.EnumWindows(enum_windows_callback, vnc_windows)

# Create the application
app = QApplication([])

# Create and show the window
window = Window(vnc_windows)
window.show()

# Run the event loop
sys.exit(app.exec_())