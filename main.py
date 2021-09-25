# coding=utf-8
import itchat
from itchat.content import *

import manager
from plugin import chat, repeater, helper, weather, hitokoto, daily, joke, zhihu, leetcode, word_cloud, rank
from util import log


def init_commands():
    manager.set_text_command(func=helper.get_help, is_at=True, keys=(u'帮助', u'功能', 'help'))
    manager.set_text_command(func=weather.get_weather, is_at=True, keys=(u'天气', 'weather'))
    manager.set_text_command(func=hitokoto.get_hitokoto, is_at=True, keys=(u'一言', 'hitokoto'))
    manager.set_text_command(func=daily.get_daily, is_at=True, keys=(u'每日一句', 'daily'))
    manager.set_text_command(func=joke.get_joke, is_at=True, keys=(u'笑话', 'joke'))
    manager.set_text_command(func=zhihu.get_zhihu, is_at=True, keys=(u'知乎', 'zhihu'))
    manager.set_text_command(func=leetcode.get_random_problem, is_at=True, keys=(u'力扣', u'随机一题', 'leetcode'))
    manager.set_text_command(func=word_cloud.get_word_cloud, is_at=True, keys=(u'词云', 'wordcloud'))
    manager.set_text_command(func=rank.get_rank_list, is_at=True, keys=(u'天梯', 'rank'))
    manager.set_text_command(func=chat.get_chat_reply, is_at=True)
    manager.set_text_command(func=repeater.get_repeated_text, is_at=False)
    manager.set_img_command(func=repeater.get_repeated_img)


@itchat.msg_register(TEXT, isGroupChat=True)
def group_text_reply(msg):
    log.log(msg)
    return manager.get_text_reply(msg)


@itchat.msg_register(PICTURE, isGroupChat=True)
def group_msg_reply(msg):
    return manager.get_img_reply(msg)


if __name__ == '__main__':
    init_commands()
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    itchat.run()
