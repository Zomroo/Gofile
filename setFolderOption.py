import requests
import config

def set_folder_option(folder_id, option, value):
    url = "https://api.gofile.io/setFolderOption"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Token": config.GOFILE_API_KEY
    }

    data = {
        "folderId": folder_id,
        "option": option,
        "value": value
    }

    response = requests.put(url, headers=headers, data=data)
    response_json = response.json()

    if response_json['status'] == 'ok':
        return True
    else:
        return False
