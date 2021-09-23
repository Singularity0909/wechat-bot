# coding=utf-8
import requests

API_URL = 'https://www.mxnzp.com/api/jokes/list/random'
HEADERS = {'app_id': 'lbeqhqhnhgo22otp', 'app_secret': 'OFpUMnhWOEhoVWNkM3dOaVV2dnhQQT09'}


def get_joke(msg):
    try:
        resp = requests.get(API_URL, headers=HEADERS)
        assert resp.status_code == 200
        return resp.json()['log'][0]['content']
    except:
        return u'获取失败'
