# -*- coding: utf-8 -*-
import requests
import pprint
import re

def post_chat(title, contents):
    apikey = '5d885ec366178e84854d76e4a19f5784'
    endpoint = 'https://api.chatwork.com/v2'
    roomid = '173813291'

    comp = re.compile(r"<[^>]*?>")
    comptxt = comp.sub("", contents)

    post_message_url = '{}/rooms/{}/messages'.format(endpoint, roomid)
    chattag = "[To:4094042] hirata[info][title]{}[/title]{}[/info]"
    headers = { 'X-ChatWorkToken': apikey }
    params = { 'body': chattag.format(title.encode('utf-8'), comptxt.encode('utf-8')) }

    resp = requests.post(post_message_url, headers=headers, params=params)

    pprint.pprint(resp.content)

    #return data['access']['token']['id']
