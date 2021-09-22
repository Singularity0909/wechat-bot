# coding=utf8
import os

import requests


def download_image(url, path):
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
