# coding=utf8
import time

import itchat

import chat
import hitokoto
import repeater
import weather


@itchat.msg_register('Text', isGroupChat=True)
def group_text_reply(msg):
    text = msg['Text']
    if msg['isAt']:
        print('%s %s %s' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg['ActualNickName'], text))
        prefix = u'@%s\u2005' % msg['ActualNickName']
        if u'天气' in text:
            info = weather.get_weather(text)
            if info:
                return prefix + info
        elif u'一言' in text:
            return prefix + hitokoto.get_hitokoto()
        elif u'源代码' in text:
            return prefix + u'你可以在这里了解我：https://github.com/Singularity0909/wechat-bot'
        return prefix + chat.get_chat_reply(msg)
    if repeater.is_repeat(msg):
        return text


itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.run()
