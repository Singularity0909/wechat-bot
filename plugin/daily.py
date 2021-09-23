# coding=utf-8
import os

import itchat
import requests

from util import image

API_URL = 'http://open.iciba.com/dsapi/'
IMG_SAVE_PATH = 'temp'


def get_daily(msg):
    try:
        resp = requests.get(API_URL)
        assert resp.status_code == 200
        resp_json = resp.json()
        eng, ch, pic = resp_json['content'], resp_json['note'], resp_json['picture2']
        file_name = image.download_image(pic, IMG_SAVE_PATH)
        if file_name:
            itchat.send_image(os.path.join(IMG_SAVE_PATH, file_name), msg['FromUserName'])
        return eng + '\n' + ch
    except:
        return u'获取失败'
