import requests
import xml.etree.ElementTree as ET
import urllib.parse


WEBDAV_URL = "http://*/dav"
USERNAME = "*"
PASSWORD = "*"

TARGET_FOLDER = "/" 
REMOVE_PREFIX = f"dav/{TARGET_FOLDER}/" 


def get_file_list():
    folder_url = f"{WEBDAV_URL}/{TARGET_FOLDER}/"
    headers = {"Depth": "1"} 
    response = requests.request("PROPFIND", folder_url, auth=(USERNAME, PASSWORD), headers=headers)

    if response.status_code != 207:
        print(f"fail: {response.status_code}")
        return []


    response.encoding = response.apparent_encoding
    root = ET.fromstring(response.text)
    namespace = {"d": "DAV:"}

    file_list = []
    for response in root.findall("d:response", namespace):
        href = response.find("d:href", namespace).text
        file_path = urllib.parse.unquote(href).strip("/") 




        if file_path == REMOVE_PREFIX.strip("/"):
            continue


        if file_path.startswith(REMOVE_PREFIX):
            relative_path = file_path[len(REMOVE_PREFIX):]  
         

            if "/" not in relative_path and "." in relative_path:
                file_list.append(relative_path)

    return file_list


files = get_file_list()
print("list:")
for file in files:
    print(file)


