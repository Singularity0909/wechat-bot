# coding=utf-8
import requests

API_URL = 'https://v1.hitokoto.cn'


def get_hitokoto(msg):
    try:
        resp = requests.get(API_URL)
        assert resp.status_code == 200
        info_content = resp.json()['hitokoto']
        info_from = resp.json()['from']
        return info_content + ' —— ' + info_from
    except:
        return u'获取失败'
