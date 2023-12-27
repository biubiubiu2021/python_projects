import os
import getpass
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox


# Create QApplication
app = QApplication(sys.argv)

# Define your users and passwords
username1 = "amr\\666lab_raspdcg"
password1 = "Teawithrabbit@345678"

username2 = "amr\\sys_paivauto"
password2 = "Autoxpiv@1Autoxpiv@1"

username3 = ".\\general"
password3 = "Passw0rd"

credentials = {
    username1: password1,
    username2: password2,
    username3: password3
}
credentials_updated = {}
print("original credential--->\n",credentials)

# Get the current username
username = getpass.getuser()

# Get the path to the user's home directory
user_folder = os.path.expanduser("~")

# Now you can continue to check for the file in the user's home directory
filename = "NUCwindows_account.txt"
file_path = os.path.join(user_folder, filename)

# Define your default information
default_info = f"""username1 = "{username1}"
password1 = "{password1}"

username2 = "{username2}"
password2 = "{password2}"

username3 = "{username3}"
password3 = "{password3}"
"""

# Check if the file doesn't exist or if it's empty
if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
    # If it doesn't exist or is empty, write the default info
    with open(file_path, 'w') as file:
        file.write(default_info)
else:
    # If the file exists and is not empty, check if it contains three users
    with open(file_path, 'r') as file:
        #contents_ALL = file.read()
        contents = file.readlines()
        print(file_path, filename)

        print("111content in txt:\n", contents)
        contents = [line for line in contents if line.strip() != ""]
        print("222content in txt:\n", contents)
    if len(contents) != 6:
        # If it doesn't contain three users, display a warning message
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Warning: The file does not contain three users.")
        msg.setWindowTitle("Warning")
        msg.exec_()
    else:
        # Read the file and assign the values to the variables.
        # Check each line before accessing the list elements.
        print("content in txt:\n", contents)
        if isinstance(contents[0], str) and '"' in contents[0]:
            username11 = contents[0].split('"')[1]
            print("--->", username11)
        if isinstance(contents[1], str) and '"' in contents[1]:
            password11 = contents[1].split('"')[1]

        if isinstance(contents[2], str) and '"' in contents[2]:
            username22 = contents[2].split('"')[1]
        if isinstance(contents[3], str) and '"' in contents[3]:
            password22 = contents[3].split('"')[1]

        if isinstance(contents[4], str) and '"' in contents[4]:
            username33 = contents[4].split('"')[1]
        if isinstance(contents[5], str) and '"' in contents[5]:
            password33 = contents[5].split('"')[1]

        print("--->", username11)
        credentials_updated = {
            username11: password11,
            username22: password22,
            username33: password33
        }
        print("updated credential--->\n",credentials_updated)
# Execute QApplication
sys.exit(app.exec_())