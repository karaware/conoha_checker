import requests
import json
import tokens

def get_notice():
    token = tokens.get_token()
    #url = "https://account.tyo2.conoha.io/v1/b43d298cf63d469199bfc2aad701d0dd/notifications"
    url = "https://account.tyo1.conoha.io/v1/90c47eea778a4ac588610d620ab548d9/notifications"
    response = requests.get(url,
        params = {
            'offset': '0',
            'limit': '100'
        },
        headers={
            'X-Auth-Token': token,
            'Content-Type': 'application/json'
        }
    )
    data = response.json()
    return data
