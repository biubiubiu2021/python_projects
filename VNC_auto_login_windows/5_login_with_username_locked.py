import time
import win32gui
import pyautogui
import win32con


import win32com.client
import win32con

# Callback function to retrieve VNC Viewer windows
def enum_windows_callback(hwnd, vnc_windows):
    class_name = win32gui.GetClassName(hwnd)
    window_text = win32gui.GetWindowText(hwnd)
    if "corp.intel.com (" in window_text:
        vnc_windows.append((hwnd, window_text))

# Function to automate the login process for the Windows login interface


def login_to_windows(hwnd, password):
    # Simulate an Alt key press
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    time.sleep(0.1)  # wait for the app to come to the foreground

    # Set focus to the window
    win32gui.SetForegroundWindow(hwnd)

    # Wait for the window to come into focus
    time.sleep(1)

    # Type the password, then Enter
    pyautogui.typewrite(password)
    pyautogui.press('enter')

# List to store VNC Viewer windows
vnc_windows = []

# Enumerate all top-level windows
win32gui.EnumWindows(enum_windows_callback, vnc_windows)

# Display the numbered list of VNC instances
print("VNC Instances:")
for i, (hwnd, window_text) in enumerate(vnc_windows):
    print(f"{i+1}. Window hwnd: {hwnd}, Title: {window_text}")
print("---")

# Prompt the user for their selection
selection = int(input("Enter the number of the VNC instance to autologin: ")) - 1

# Perform the login process for the selected VNC Viewer window
if 0 <= selection < len(vnc_windows):
    selected_hwnd, selected_window_text = vnc_windows[selection]
    print("Selected VNC Instance:")
    print("Window hwnd:", selected_hwnd)
    print("Title:", selected_window_text)
    print("---")
    # Perform the login process for the Windows login interface within the selected VNC Viewer window
    login_to_windows(selected_hwnd,  "Autoxpiv@1Autoxpiv@1")
    time.sleep(2)
else:
    print("Invalid selection. Please try again.")