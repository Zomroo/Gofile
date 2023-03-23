import requests
import config

def get_account_details():
    url = "https://api.gofile.io/getAccountDetails"

    headers = {
        "Token": config.GOFILE_API_KEY
    }

    response = requests.get(url, headers=headers)
    response_json = response.json()

    if response_json['status'] == 'ok':
        return response_json['data']
    else:
        return None
