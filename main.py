# coding=utf8
import time

import itchat

import manager
from plugin import chat, repeater, helper, weather, hitokoto, daily, joke, zhihu, leetcode


@itchat.msg_register('Text', isGroupChat=True)
def group_text_reply(msg):
    print('%s %s %s' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), msg['ActualNickName'], msg['Text']))
    resp = manager.get_response(msg)
    if resp:
        return resp


manager.set_command([u'帮助', u'功能', 'help'], True, False, helper.get_help)
manager.set_command([u'天气', 'weather'], True, False, weather.get_weather)
manager.set_command([u'一言', 'hitokoto'], True, False, hitokoto.get_hitokoto)
manager.set_command([u'每日一句', 'daily'], True, False, daily.get_daily)
manager.set_command([u'笑话', 'joke'], True, False, joke.get_joke)
manager.set_command([u'知乎', 'zhihu'], True, False, zhihu.get_zhihu)
manager.set_command([u'力扣', u'随机一题', 'leetcode'], True, False, leetcode.get_random_problem)
manager.set_command(None, True, True, chat.get_chat_reply)
manager.set_command(None, False, True, repeater.get_repeat)

if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    itchat.run()
