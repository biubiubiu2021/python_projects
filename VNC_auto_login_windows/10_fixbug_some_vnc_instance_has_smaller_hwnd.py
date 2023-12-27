import win32gui
import pyautogui

# Callback function to retrieve VNC Viewer windows
def enum_windows_callback(hwnd, vnc_windows):
    class_name = win32gui.GetClassName(hwnd)
    window_text = win32gui.GetWindowText(hwnd)
    if "VNC Viewer" in window_text:
        vnc_windows.append((hwnd, window_text))

def switch_account(hwnd):
    # Bring the window to the front
    win32gui.SetForegroundWindow(hwnd)

    # Click on the account switch button (coordinates need to be updated)
    pyautogui.click(x=100, y=100)

    # Type the username (update with actual username)
    pyautogui.write('username')

    # Press TAB to switch to the password field
    pyautogui.press('tab')

    # Type the password (update with actual password)
    pyautogui.write('password')

    # Press ENTER to submit the form
    pyautogui.press('enter')

# List to store VNC Viewer windows
vnc_windows = []

# Enumerate all top-level windows
win32gui.EnumWindows(enum_windows_callback, vnc_windows)

print("--->", vnc_windows)
# Loop through each VNC Viewer window and display its hwnd and window text
for hwnd, window_text in vnc_windows:
    print("Window hwnd:", hwnd)
    print("Window Text:", window_text)
    print("---")
    switch_account(hwnd)

