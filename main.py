# coding=utf8
import time

import itchat

import chat
import command
import helper
import hitokoto
import repeater
import weather

command.set_command([u'帮助', u'功能', 'help'], True, False, helper.get_help)
command.set_command([u'天气', 'weather'], True, False, weather.get_weather)
command.set_command([u'一言', 'hitokoto'], True, False, hitokoto.get_hitokoto)
command.set_command(None, True, True, chat.get_chat_reply)
command.set_command(None, False, True, repeater.get_repeat)


@itchat.msg_register('Text', isGroupChat=True)
def group_text_reply(msg):
    print('%s %s %s' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg['ActualNickName'], msg['Text']))
    resp = command.get_response(msg)
    if resp:
        return resp


itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.run()
