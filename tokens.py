import requests
import json

def get_token():
    endpoint = 'https://identity.tyo2.conoha.io/v2.0/tokens'
    headers = {'Accept': 'application/json'}
    user = 'gncu24186166'
    passwd = 'r34RBTe7eepE'
    tid = 'b43d298cf63d469199bfc2aad701d0dd'
    body = {"auth": {"passwordCredentials": {"username": user, "password": passwd}, "tenantId": tid}}

    resp = requests.post(endpoint, data=json.dumps(body), headers=headers)

    data = resp.json()
    #print(data['access']['token']['id'])

    return data['access']['token']['id']
