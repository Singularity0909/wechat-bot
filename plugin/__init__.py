# coding=utf-8
import os

STOPWORDS_PATH = 'data'

STOPWORDS_FILE_NAMES = (
    'baidu_stopwords.txt',
    'cn_stopwords.txt',
    'hit_stopwords.txt',
    'scu_stopwords.txt'
)

stopword_set = set()

for file_name in STOPWORDS_FILE_NAMES:
    with open(os.path.join(STOPWORDS_PATH, file_name), 'r', encoding='utf-8') as f:
        for line in f.readlines():
            stopword_set.add(line.strip())
        f.close()
print(u'停用词加载完成')
