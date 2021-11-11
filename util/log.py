# coding=utf-8
import os
import time

LOG_FILE_PATH = 'log'


def get_current_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


def get_log_file_name(msg):
    return "%s%s.txt" % (time.strftime('%Y-%m-%d', time.localtime()), msg['FromUserName'])


def log(msg):
    print(get_current_time(), msg['ActualNickName'], msg['Text'])
    if not os.path.exists(LOG_FILE_PATH):
        os.makedirs(LOG_FILE_PATH)
    with open(os.path.join(LOG_FILE_PATH, get_log_file_name(msg)), 'a+', encoding='utf-8') as f:
        f.write('@%s %s@\n%s\n' % (get_current_time(), msg['ActualNickName'], msg['Text']))
        f.close()


def get_today_text(msg):
    path = os.path.join(LOG_FILE_PATH, get_log_file_name(msg))
    if not os.path.exists(path):
        return None
    resp = ''
    with open(path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if line.startswith('@') and line.endswith('@\n'):
                continue
            resp += line
        f.close()
    return resp


def get_nickname_by_log(line):
    len_ = len(line)
    idx_left, idx_right = 0, len_ - 3
    count = 0
    for idx in range(len(line)):
        if line[idx] == ' ':
            count += 1
            if count == 2:
                idx_left = idx + 1
                break
    return line[idx_left:idx_right + 1]


def get_today_count_map(msg):
    count_map = {}
    path = os.path.join(LOG_FILE_PATH, get_log_file_name(msg))
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            for line in f.readlines():
                if line.startswith('@') and line.endswith('@\n'):
                    nickname = get_nickname_by_log(line)
                    if not count_map.get(nickname):
                        count_map[nickname] = 0
                    count_map[nickname] += 1
            f.close()
    return count_map
