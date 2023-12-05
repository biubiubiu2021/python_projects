import pyautogui
import win32gui
import time
import win32con
from PIL import Image
import win32com.client

# Callback function to retrieve VNC Viewer windows
def enum_windows_callback(hwnd, vnc_windows):
    class_name = win32gui.GetClassName(hwnd)
    window_text = win32gui.GetWindowText(hwnd)
    if "VNC Viewer" in window_text and not window_text.startswith("VNC Viewer"):
        # Consider only the part of the title before the first space followed by a hyphen or parenthesis
        title_key = window_text.split(" -")[0].split(" (")[0]
        # If the title_key is not in the dictionary, or the current hwnd is larger and the existing title does not have parentheses, or the current title has parentheses, add/update it
        if title_key not in vnc_windows or ("(" not in vnc_windows[title_key][1] and hwnd > vnc_windows[title_key][0]) or "(" in window_text:
            vnc_windows[title_key] = (hwnd, window_text)


from PIL import Image
import win32com.client

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

    # Capture a 200x200 region around the center
    im = pyautogui.screenshot(region=(center_x - 200, center_y - 10, 400, 150))
    im.save(f'{window_text}.png')

    # Display the image
    img = Image.open(f'{window_text}.png')
    img.show()



# Dictionary to store VNC Viewer windows
vnc_windows = {}

# Enumerate all top-level windows
win32gui.EnumWindows(enum_windows_callback, vnc_windows)
print("--->\n", vnc_windows)

# Display the numbered list of VNC instances
print("VNC Instances:")
for i, (window_text, (hwnd, _)) in enumerate(vnc_windows.items()):
    print(f"{i+1}. Window hwnd: {hwnd}, Title: {window_text}")
print("---")

# Take a screenshot of each VNC Viewer window
for window_text, (hwnd, _) in vnc_windows.items():
    take_screenshot(hwnd, window_text)