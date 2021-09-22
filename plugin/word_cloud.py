# coding=utf-8
import os

import itchat
import jieba
from wordcloud import WordCloud

from util import data

FONT_PATH = 'font'
FONT_FILE_NAME = 'msyh.ttf'
IMG_SAVE_PATH = 'temp'
IMG_FILE_NAME = 'word_cloud.png'


def get_word_cloud(msg):
    try:
        text = data.get_today_text(msg)
        words = ' '.join(jieba.cut(text, cut_all=False))
        word_cloud = WordCloud(background_color="white", width=1000, height=800, margin=2,
                               font_path=os.path.join(FONT_PATH, FONT_FILE_NAME)).generate(words)
        word_cloud.to_file(os.path.join(IMG_SAVE_PATH, IMG_FILE_NAME))
        itchat.send_image(os.path.join(IMG_SAVE_PATH, IMG_FILE_NAME), msg['FromUserName'])
        return None
    except:
        return u'生成失败'
