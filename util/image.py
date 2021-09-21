# coding=utf8
import requests


def download_image(url):
    try:
        file_name = url.split('/')[-1]
        resp = requests.get(url, stream=True)
        assert resp.status_code == 200
        open('temp/' + file_name, 'wb').write(resp.content)
        return file_name
    except:
        return None
