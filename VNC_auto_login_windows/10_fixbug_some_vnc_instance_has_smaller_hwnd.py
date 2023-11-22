import time
import win32gui
import pyautogui
import win32com.client
import win32con



credentials = [
    ("amr\lab_raspdcg", "Teawithrabbit@345678"),
    ("amr\sys_paivauto", "Autoxpiv@1Autoxpiv@1"),
    # Add more as needed
]
# Display the available sets of credentials
print("Available sets of credentials:")
for i, (username, password) in enumerate(credentials):
    print(f"{i+1}. Username: {username}, Password: {password}")
print("---")

# Prompt the user to select a set of credentials
cred_selection = int(input("Enter the number of the set of credentials to use: ")) - 1

# Validate the selection
if 0 <= cred_selection < len(credentials):
    selected_username, selected_password = credentials[cred_selection]
else:
    print("Invalid selection. Please try again.")
    exit()

# Callback function to retrieve VNC Viewer windows
# Callback function to retrieve VNC Viewer windows
def enum_windows_callback(hwnd, vnc_windows):
    class_name = win32gui.GetClassName(hwnd)
    window_text = win32gui.GetWindowText(hwnd)
    if "VNC Viewer" in window_text and not window_text.startswith("VNC Viewer -"):
        # Consider only the part of the title before the first space followed by a hyphen or parenthesis
        title_key = window_text.split(" -")[0].split(" (")[0]
        # If the title_key is not in the dictionary, or the current hwnd is larger and the existing title does not have parentheses, or the current title has parentheses, add/update it
        if title_key not in vnc_windows or ("(" not in vnc_windows[title_key][1] and hwnd > vnc_windows[title_key][0]) or "(" in window_text:
            vnc_windows[title_key] = (hwnd, window_text)


# Function to automate the login process for the Windows login interface when the username is not filled in
def login_to_windows_with_username(hwnd, username, password):
    # Simulate an Alt key press
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    time.sleep(0.1)  # wait for the app to come to the foreground

    # Set focus to the window
    win32gui.SetForegroundWindow(hwnd)

    # Wait for the window to come into focus
    time.sleep(1)

    # Type the username, followed by Tab
    pyautogui.typewrite(username)
    pyautogui.press('tab')

    # Type the password, then Enter
    pyautogui.typewrite(password)
    pyautogui.press('enter')

# Function to automate the login process for the Windows login interface when the username is already filled in
def login_to_windows_without_username(hwnd, password):
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
vnc_windows = {}

# Enumerate all top-level windows
win32gui.EnumWindows(enum_windows_callback, vnc_windows)
print("--->\n", vnc_windows)
# Display the numbered list of VNC instance
print("VNC Instances:")
for i, (window_text, (hwnd, _)) in enumerate(vnc_windows.items()):
    print(f"{i+1}. Window hwnd: {hwnd}, Title: {window_text}")
print("---")

# Prompt the user for their selection
selection = int(input("Enter the number of the VNC instance to autologin: ")) - 1
username_filled = input("Is the username already filled in? (yes/no): ").lower()

# Perform the login process for the selected VNC Viewer window
if 0 <= selection < len(vnc_windows):
    selected_window_text, (selected_hwnd, _) = list(vnc_windows.items())[selection]
    print("Selected VNC Instance:")
    print("Window hwnd:", selected_hwnd)
    print("Title:", selected_window_text)
    print("---")
    # Perform the login process for the Windows login interface within the selected VNC Viewer window
    if username_filled == 'yes':
        login_to_windows_without_username(selected_hwnd, selected_password)
    else:
        login_to_windows_with_username(selected_hwnd, selected_username, selected_password)
    time.sleep(2)
else:
    print("Invalid selection. Please try again.")