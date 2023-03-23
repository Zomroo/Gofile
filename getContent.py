import requests
import config

def get_file_content(file_id):
    url = f"https://api.gofile.io/getContent?contentId={file_id}&token={config.GOFILE_API_KEY}"

    response = requests.get(url)
    response_json = response.json()

    if response_json['status'] == 'ok':
        return response_json['data']
    else:
        return None
