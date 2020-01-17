import requests
import pprint
import re

def post_chat(title, contents):
    apikey = '5d885ec366178e84854d76e4a19f5784' #ビヨンド自動通知くん
    endpoint = 'https://api.chatwork.com/v2'
    roomid = '173813291'

    comp = re.compile(r"<[^>]*?>")
    comptxt = comp.sub("", contents)

    post_message_url = '{}/rooms/{}/messages'.format(endpoint, roomid)
    chattag = "[To:4094042] 平田[info][title]{}[/title]{}[/info]"
    headers = { 'X-ChatWorkToken': apikey }
    params = { 'body': chattag.format(title, comptxt) }

    resp = requests.post(post_message_url, headers=headers, params=params)

    pprint.pprint(resp.content)

    #return data['access']['token']['id']
