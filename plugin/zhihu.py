# coding=utf8
import requests

API_URL = 'https://news-at.zhihu.com/api/4/news/latest'
STORY_URL_FORMAT = 'https://daily.zhihu.com/story/{}'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


def get_zhihu(msg):
    try:
        resp = requests.get(API_URL, headers=HEADERS)
        assert resp.status_code == 200
        data = resp.json()
        stories = data.get('stories')
        if not stories:
            return u'暂时没有数据，或者服务无法访问'
        reply = u'今天的知乎日报：\n'
        for story in stories:
            url = STORY_URL_FORMAT.format(story['id'])
            title = story.get('title', u'未知内容')
            reply += f'\n{title}\n{url}\n'
        return reply.strip()
    except:
        return u'获取失败'
