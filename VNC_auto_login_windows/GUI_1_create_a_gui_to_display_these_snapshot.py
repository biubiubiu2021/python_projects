import time
import win32gui
import pyautogui
import win32com.client
import win32con
import os

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

from PyQt5.QtGui import QPixmap
import sys


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
    im = pyautogui.screenshot(region=(center_x - 200, center_y - 10, 400, 150))

    # Ensure the directory exists
    os.makedirs('C:/tmp/', exist_ok=True)

    # Save the screenshot in the C:/tmp/ directory with the filename set to the hwnd
    im.save(os.path.join('C:/tmp/', f'{hwnd}.png'))


class Window(QWidget):
    def __init__(self, vnc_windows):
        super().__init__()

        self.setWindowTitle("VNC Viewer")
        self.setGeometry(100, 100, 400, 600)

        layout = QVBoxLayout()

        for window_text, (hwnd, _) in vnc_windows.items():
            # Load the image
            pixmap = QPixmap(os.path.join('C:/tmp/', f'{hwnd}.png'))

            # Resize the QPixmap
            pixmap_resized = pixmap.scaled(300, 100)

            # Create a vertical layout for the title and image
            v_layout = QVBoxLayout()

            # Create a label with the window title
            title_label = QLabel(window_text, self)
            v_layout.addWidget(title_label)

            # Create a label with the image
            image_label = QLabel(self)
            image_label.setPixmap(pixmap_resized)
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

# Dictionary to store VNC Viewer windows
vnc_windows = {}

# Enumerate all top-level windows
win32gui.EnumWindows(enum_windows_callback, vnc_windows)

# Take a screenshot of each VNC Viewer window
for window_text, (hwnd, _) in vnc_windows.items():
    take_screenshot(hwnd, window_text)

# Create the application
app = QApplication([])

# Create and show the window
window = Window(vnc_windows)
window.show()

# Run the event loop
sys.exit(app.exec_())