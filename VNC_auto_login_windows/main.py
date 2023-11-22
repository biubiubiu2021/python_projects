import pyautogui
import time
from screeninfo import get_monitors

def get_display_coordinates(x, y, display):
    monitors = get_monitors()
    if display <= len(monitors):
        monitor = monitors[display - 1]
        return monitor.x + x, monitor.y + y
    else:
        raise ValueError("Invalid display number")

def autofill_windows_login(username, windows_password, display=1):
    # Wait for the Windows login window to appear within the VNC session
    time.sleep(5)

    # Calculate the coordinates on the specified display
    username_x, username_y = get_display_coordinates(500, 400, display)
    password_x, password_y = get_display_coordinates(500, 500, display)

    # Move the mouse to the Windows username field on the specified display and click on it
    pyautogui.moveTo(username_x, username_y)
    pyautogui.click()

    # Type the Windows username
    pyautogui.typewrite(username)

    # Move the mouse to the Windows password field on the specified display and click on it
    pyautogui.moveTo(password_x, password_y)
    pyautogui.click()

    # Type the Windows password
    pyautogui.typewrite(windows_password)

    # Press Enter to submit the Windows login
    pyautogui.press('enter')

# Usage: Call the autofill_windows_login function with your username, Windows password, and display number as arguments
autofill_windows_login("amr\sys_paivauto", "Autoxpiv@1Autoxpiv@1", display=1)