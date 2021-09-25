# coding=utf-8
import os
from dataclasses import dataclass
from typing import Dict

import itchat

from util import file

IMG_SAVE_PATH = 'temp'


@dataclass
class Record:
    last_text: str
    last_img: str
    repeated: bool


records: Dict[str, Record] = {}


def get_repeated_text(msg):
    text = msg['Text']
    record = records.get(msg['FromUserName'])
    if not record or record.last_text != text:
        record = Record(last_text=text, last_img='', repeated=False)
        records[msg['FromUserName']] = record
    elif not record.repeated and record.last_text == text:
        record.repeated = True
        return text
    return None


def get_repeated_img(msg):
    file_name = msg['FileName']
    msg.download(os.path.join(IMG_SAVE_PATH, file_name))
    hash_ = file.get_md5(os.path.join(IMG_SAVE_PATH, file_name))
    record = records.get(msg['FromUserName'])
    if not record or record.last_img != hash_:
        record = Record(last_text='', last_img=hash_, repeated=False)
        records[msg['FromUserName']] = record
    elif not record.repeated and record.last_img == hash_:
        record.repeated = True
        itchat.send_image(os.path.join(IMG_SAVE_PATH, file_name), msg['FromUserName'])
    if os.path.isfile(os.path.join(IMG_SAVE_PATH, file_name)):
        os.remove(os.path.join(IMG_SAVE_PATH, file_name))
    return None
