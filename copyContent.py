import requests
import config

def copy_content(content_id, folder_id_dest):
    url = "https://api.gofile.io/copyContent"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Token": config.GOFILE_API_KEY
    }

    data = {
        "contentsId": content_id,
        "folderIdDest": folder_id_dest
    }

    response = requests.put(url, headers=headers, data=data)
    response_json = response.json()

    if response_json['status'] == 'ok':
        return response_json['data']['newContentsId']
    else:
        return None
