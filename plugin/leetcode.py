# coding=utf-8
import random

import requests

PROBLEM_PAGE_URL_FORMAT = 'https://leetcode-cn.com/problems/{}'
PROBLEM_LIST_API_URL = 'https://leetcode-cn.com/api/problems/algorithms/'


def get_random_problem(msg):
    try:
        resp = requests.get(PROBLEM_LIST_API_URL)
        assert resp.status_code == 200
        data = resp.json()
        num_total = data['num_total']
        idx = random.randint(0, num_total - 1)
        stat = data['stat_status_pairs'][idx]['stat']
        id = stat['question_id']
        title = stat['question__title']
        slug = stat['question__title_slug']
        return '%d. %s %s' % (id, title, PROBLEM_PAGE_URL_FORMAT.format(slug))
    except:
        return u'获取失败'
