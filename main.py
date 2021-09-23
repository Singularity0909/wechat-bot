# coding=utf8
import itchat

import manager
from plugin import chat, repeater, helper, weather, hitokoto, daily, joke, zhihu, leetcode, word_cloud, rank
from util import log

manager.set_command(func=helper.get_help, is_at=True, keys=[u'帮助', u'功能', 'help'])
manager.set_command(func=weather.get_weather, is_at=True, keys=[u'天气', 'weather'])
manager.set_command(func=hitokoto.get_hitokoto, is_at=True, keys=[u'一言', 'hitokoto'])
manager.set_command(func=daily.get_daily, is_at=True, keys=[u'每日一句', 'daily'])
manager.set_command(func=joke.get_joke, is_at=True, keys=[u'笑话', 'joke'])
manager.set_command(func=zhihu.get_zhihu, is_at=True, keys=[u'知乎', 'zhihu'])
manager.set_command(func=leetcode.get_random_problem, is_at=True, keys=[u'力扣', u'随机一题', 'leetcode'])
manager.set_command(func=word_cloud.get_word_cloud, is_at=True, keys=[u'词云', 'wordcloud'])
manager.set_command(func=rank.get_rank_list, is_at=True, keys=[u'天梯', 'rank'])
manager.set_command(func=chat.get_chat_reply, is_at=True)
manager.set_command(func=repeater.get_repeat, is_at=False)


@itchat.msg_register('Text', isGroupChat=True)
def group_text_reply(msg):
    log.log(msg)
    return manager.get_response(msg)


if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    itchat.run()
