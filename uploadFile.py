import requests
import config

def upload_file(file_path):
    url = "https://store1.gofile.io/uploadFile"

    headers = {
        "Content-Type": "multipart/form-data",
        "Token": config.GOFILE_API_KEY
    }

    # Open the file in binary mode and read its contents
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Set up the multipart/form-data payload for the request
    payload = {
        "file": ("file", file_data)
    }

    response = requests.post(url, headers=headers, files=payload)
    response_json = response.json()

    if response_json['status'] == 'ok':
        return response_json['data']['downloadPage']
    else:
        return None
