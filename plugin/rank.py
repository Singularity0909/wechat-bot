# coding=utf-8
from util import log

TOP_NUMBER = 10


def get_rank_list(msg):
    try:
        count_map = log.get_today_count_map(msg)
        pairs = []
        for key, val in count_map.items():
            pairs.append((val, key))
        pairs.sort(reverse=True)
        reply = u'今日天梯 🏆\n\n'
        for idx in range(min(len(pairs), TOP_NUMBER)):
            nickname, count = pairs[idx][1], pairs[idx][0]
            reply += u'%s %d 次\n' % (nickname, count)
        return reply
    except:
        return u'获取失败'
