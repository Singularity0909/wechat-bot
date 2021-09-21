# coding=utf8
import random
import re

import requests

EXPR_DONT_UNDERSTAND = (
    '我现在还不太明白你在说什么呢，但没关系，以后的我会变得更聪明呢！',
    '我有点看不懂你的意思呀，可以跟我聊些简单的话题嘛 =。=',
    '其实我不太明白你的意思……',
    '抱歉哦，我现在的能力还不能够明白你在说什么，但我会加油的～',
    '唔……等会再告诉你'
)


def get_chat_reply(msg):
    try:
        prefix = u'@%s' % msg['User']['Self']['NickName']
        text = msg['Text'].replace(prefix, '').strip()
        url = 'http://nlp.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=%7B%22sessionId%22%3A%226fbcb6cc41e2470b806f22ee195754b9%22%2C%22robotId%22%3A%22webbot%22%2C%22userId%22%3A%22dda77818b04e4ad79a9d3836b6483e03%22%2C%22body%22%3A%7B%22content%22%3A%22' + text + '%22%7D%2C%22type%22%3A%22txt%22%7D'
        resp = requests.get(url)
        contents = re.findall(r'\"content\":\"(.+?)\\r\\n\"', resp.content.decode())
        if contents[-1] == 'defaultReply':
            return random.choice(EXPR_DONT_UNDERSTAND)
        return contents[-1]
    except:
        return random.choice(EXPR_DONT_UNDERSTAND)
