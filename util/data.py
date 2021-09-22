# coding=utf-8
import os
import time

LOG_FILE_PATH = 'data'


def get_current_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


def get_log_file_name(msg):
    return "%s%s.txt" % (time.strftime('%Y-%m-%d', time.localtime()), msg['FromUserName'])


def log(msg):
    print(get_current_time(), msg['ActualNickName'], msg['Text'])
    if not os.path.exists(LOG_FILE_PATH):
        os.makedirs(LOG_FILE_PATH)
    with open(os.path.join(LOG_FILE_PATH, get_log_file_name(msg)), 'a+') as f:
        f.write('@%s %s@\n%s\n' % (get_current_time(), msg['ActualNickName'], msg['Text']))
        f.close()


def get_today_text(msg):
    path = os.path.join(LOG_FILE_PATH, get_log_file_name(msg))
    if not os.path.exists(path):
        return None
    resp = ''
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('@') and line.endswith('@\n'):
                continue
            resp += line
        f.close()
    return resp
