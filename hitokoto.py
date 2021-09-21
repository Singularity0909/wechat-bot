# coding=utf8
import requests


def get_hitokoto():
    try:
        resp = requests.get('https://v1.hitokoto.cn')
        info_content = resp.json()['hitokoto']
        info_from = resp.json()['from']
        return info_content + ' —— ' + info_from
    except:
        return u'获取失败'
