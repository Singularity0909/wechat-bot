# coding=utf8
import itchat
import requests

from util import image

API_URL = 'http://open.iciba.com/dsapi/'


def get_daily(msg):
    try:
        url = API_URL
        resp = requests.get(url)
        assert resp.status_code == 200
        resp_json = resp.json()
        eng = resp_json['content']
        ch = resp_json['note']
        pic = resp_json['picture2']
        file_name = image.download_image(pic, 'temp/')
        if file_name:
            itchat.send('@img@temp/' + file_name, msg['FromUserName'])
        return eng + '\n' + ch
    except:
        return u'获取失败'
