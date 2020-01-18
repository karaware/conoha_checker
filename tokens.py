import requests
import json

def get_token():
    #endpoint = 'https://identity.tyo2.conoha.io/v2.0/tokens'
    endpoint = 'https://identity.tyo1.conoha.io/v2.0/tokens'
    headers = {'Accept': 'application/json'}
    #user = 'gncu24186166' #hirata_private_user
    #passwd = 'r34RBTe7eepE' #hirata_private_pass
    #tid = 'b43d298cf63d469199bfc2aad701d0dd' #hirata_private_tid
    user = 'gncu75911015'
    passwd = 'Kc29Jf5wgn5RqmCG'
    tid = '90c47eea778a4ac588610d620ab548d9'

    body = {"auth": {"passwordCredentials": {"username": user, "password": passwd}, "tenantId": tid}}

    resp = requests.post(endpoint, data=json.dumps(body), headers=headers)

    data = resp.json()

    return data['access']['token']['id']
