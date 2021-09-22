# coding=utf8
import requests

API_URL = 'https://www.mxnzp.com/api/jokes/list/random'


def get_joke(msg):
    url = API_URL
    headers = {'app_id': 'lbeqhqhnhgo22otp', 'app_secret': 'OFpUMnhWOEhoVWNkM3dOaVV2dnhQQT09'}
    resp = requests.get(url, headers=headers)
    return resp.json()['data'][0]['content']
