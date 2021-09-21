# coding=utf8
import itchat
import requests

from util import image


def get_daily(msg):
    url = 'http://open.iciba.com/dsapi/'
    resp = requests.get(url)
    resp_json = resp.json()
    eng = resp_json['content']
    ch = resp_json['note']
    pic = resp_json['picture2']
    file_name = image.download_image(pic)
    if file_name:
        itchat.send('@img@temp/' + file_name, msg['FromUserName'])
    return eng + '\n' + ch
