# coding=utf-8
command_text_map_at = {}
command_text_map_all = {}
command_text_at_default = None
command_text_all_default = None
command_img = None


def set_text_command(func, is_at, keys=None):
    global command_text_at_default, command_text_all_default
    if not keys:
        if is_at:
            command_text_at_default = func
        else:
            command_text_all_default = func
    elif is_at:
        for key in keys:
            command_text_map_at[key] = func
    else:
        for key in keys:
            command_text_map_all[key] = func


def get_text_command(msg):
    text = msg['Text']
    is_at = msg['isAt']
    if is_at:
        for key, val in command_text_map_at.items():
            if key in text:
                return val
        return command_text_at_default
    for key, val in command_text_map_all.items():
        if key in text:
            return val
    return command_text_all_default


def get_text_reply(msg):
    func = get_text_command(msg)
    if not func:
        return None
    body = func(msg)
    if not body:
        return None
    is_at = msg['isAt']
    prefix = ''
    if is_at:
        prefix = u'@%s\u2005' % msg['ActualNickName']
    return prefix + body


def set_img_command(func):
    global command_img
    command_img = func


def get_img_reply(msg):
    if not command_img:
        return None
    return command_img(msg)
