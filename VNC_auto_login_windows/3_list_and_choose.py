import time
import win32gui

# Callback function to retrieve VNC Viewer windows
def enum_windows_callback(hwnd, vnc_windows):
    class_name = win32gui.GetClassName(hwnd)
    window_text = win32gui.GetWindowText(hwnd)
    if "corp.intel.com (" in window_text:
        vnc_windows.append((hwnd, window_text))

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
    # Perform the login process for the selected VNC Viewer window
    login_to_windows(selected_hwnd, "your_username", "your_password")
    time.sleep(2)
else:
    print("Invalid selection. Please try again.")