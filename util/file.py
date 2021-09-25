# coding=utf-8
import hashlib
import os

import requests


def download(url, path):
    try:
        file_name = url.split('/')[-1]
        resp = requests.get(url, stream=True)
        assert resp.status_code == 200
        if not os.path.exists(path):
            os.makedirs(path)
        with open(os.path.join(path, file_name), 'wb') as f:
            f.write(resp.content)
            f.close()
        return file_name
    except:
        return None


def get_md5(file_name):
    if not os.path.isfile(file_name):
        return None
    hash_ = hashlib.md5()
    with open(file_name, 'rb') as f:
        hash_.update(f.read())
        f.close()
    return hash_.hexdigest()
