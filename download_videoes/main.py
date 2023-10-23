import requests

login_url = "https://www.mindshare.com/login"
xml_url = "https://www.mindshare.com/path/to/xml/file.xml"
username = "ziang.wang@intel.com"
password = "DCAI-CCE@CXL!"

# Create a session object to persist the login session
session = requests.Session()

# Login to Mindshare
login_data = {
    "username": username,
    "password": password
}
response = session.post(login_url, data=login_data)
if response.status_code == 200:
    print("Login successful!")
else:
    print("Login failed.")

# Download the XML file
response = session.get(xml_url)
if response.status_code == 200:
    with open("file.xml", "wb") as file:
        file.write(response.content)
    print("XML file downloaded successfully!")
else:
    print("Failed to download XML file.")