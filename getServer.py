import requests
import config

def get_gofile_server():
    url = "https://api.gofile.io/getServer"

    headers = {
        "Content-Type": "application/json",
        "Token": config.GOFILE_API_KEY
    }

    response = requests.get(url, headers=headers)
    response_json = response.json()

    if response_json['status'] == 'ok':
        return response_json['data']['server']
    else:
        return None
