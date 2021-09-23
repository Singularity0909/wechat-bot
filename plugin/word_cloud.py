# coding=utf-8
import os

import itchat
import jieba
from wordcloud import WordCloud

from plugin import stopword_set
from util import log

FONT_PATH = 'data'
FONT_FILE_NAME = 'msyh.ttf'

IMG_SAVE_PATH = 'temp'
IMG_FILE_NAME = 'word_cloud.png'


def get_word_cloud(msg):
    try:
        text = log.get_today_text(msg)
        words = ' '.join(jieba.cut(text, cut_all=False))
        WordCloud(background_color="white", width=1000, height=800, margin=2,
                  font_path=os.path.join(FONT_PATH, FONT_FILE_NAME), stopwords=stopword_set).generate(words).to_file(
            os.path.join(IMG_SAVE_PATH, IMG_FILE_NAME))
        itchat.send_image(os.path.join(IMG_SAVE_PATH, IMG_FILE_NAME), msg['FromUserName'])
        return None
    except:
        return u'生成失败'
