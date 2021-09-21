from dataclasses import dataclass
from typing import Dict


@dataclass
class Record:
    last_text: str
    repeated: bool


records: Dict[str, Record] = {}


def is_repeat(msg):
    text = msg['Text']
    record = records.get(msg['FromUserName'])
    if not record or record.last_text != text:
        record = Record(last_text=text, repeated=False)
        records[msg['FromUserName']] = record
    elif not record.repeated and record.last_text == text:
        record.repeated = True
        return True
    return False
