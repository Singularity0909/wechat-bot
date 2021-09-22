# coding=utf8
import requests

API_URL = 'https://www.mxnzp.com/api/jokes/list/random'
HEADERS = {'app_id': 'lbeqhqhnhgo22otp', 'app_secret': 'OFpUMnhWOEhoVWNkM3dOaVV2dnhQQT09'}


def get_joke(msg):
    resp = requests.get(API_URL, headers=HEADERS)
    return resp.json()['data'][0]['content']
