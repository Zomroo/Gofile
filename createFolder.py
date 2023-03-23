import requests
import config

def create_folder(folder_name, parent_folder_id=None):
    url = "https://api.gofile.io/createFolder"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Token": config.GOFILE_API_KEY
    }

    data = {
        "folderName": folder_name
    }

    if parent_folder_id:
        data["parentFolderId"] = parent_folder_id

    response = requests.put(url, headers=headers, data=data)
    response_json = response.json()

    if response_json['status'] == 'ok':
        return response_json['data']['folderId']
    else:
        return None
