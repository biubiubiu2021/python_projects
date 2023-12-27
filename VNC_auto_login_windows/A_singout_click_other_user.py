import time
import win32gui
import pyautogui

# Callback function to retrieve VNC Viewer windows
def enum_windows_callback(hwnd, vnc_windows):
    class_name = win32gui.GetClassName(hwnd)
    window_text = win32gui.GetWindowText(hwnd)
    if "VNC Viewer" in window_text and not window_text.startswith("VNC Viewer") and ("FL" in window_text or ("SR" in window_text) or ("zz" in window_text)):
        title_key = window_text.split(" -")[0].split(" (")[0]
        if title_key not in vnc_windows or ("(" not in vnc_windows[title_key][1] and hwnd > vnc_windows[title_key][0]) or "(" in window_text:
            vnc_windows[title_key] = (hwnd, window_text)

import pyautogui

def switch_account(hwnd):
    # Set the focus to the specified window
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
    #pyautogui.click(x=100, y=200)  # Replace with the actual coordinates of the 'Other user' button

    # Locate the 'Other user' button based on an image file
    time.sleep(3)
    location = pyautogui.locateOnScreen('other_user_button.png', confidence=0.8)

    # Click the 'Other user' button
    if location:
        pyautogui.click(location)
    time.sleep(1)
    # Type the username and password of the other account




# List to store VNC Viewer windows
vnc_windows = {}

# Enumerate all top-level windows
win32gui.EnumWindows(enum_windows_callback, vnc_windows)

print("--->", vnc_windows)
# Loop through each VNC Viewer window and display its hwnd and window text
for title_key, (hwnd, window_text) in vnc_windows.items():
    print("Window hwnd:", hwnd)
    print("Window Text:", window_text)
    print("---")
    switch_account(hwnd)

