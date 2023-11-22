import win32gui

# Callback function to retrieve VNC Viewer windows
def enum_windows_callback(hwnd, vnc_windows):
    class_name = win32gui.GetClassName(hwnd)
    window_text = win32gui.GetWindowText(hwnd)
    if "corp.intel.com" in window_text:
        vnc_windows.append((hwnd, window_text))

# List to store VNC Viewer windows
vnc_windows = []

# Enumerate all top-level windows
win32gui.EnumWindows(enum_windows_callback, vnc_windows)

# Loop through each VNC Viewer window and display its hwnd and window text
for hwnd, window_text in vnc_windows:
    print("Window hwnd:", hwnd)
    print("Window Text:", window_text)
    print("---")
