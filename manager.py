# coding=utf8
command_map_at = {}
command_map_all = {}
command_at_default = None
command_all_default = None


def set_command(func, is_at, keys=None):
    global command_at_default, command_all_default
    if not keys:
        if is_at:
            command_at_default = func
        else:
            command_all_default = func
    elif is_at:
        for key in keys:
            command_map_at[key] = func
    else:
        for key in keys:
            command_map_all[key] = func


def get_command(msg):
    text = msg['Text']
    is_at = msg['isAt']
    if is_at:
        for key, val in command_map_at.items():
            if key in text:
                return val
        return command_at_default
    for key, val in command_map_all.items():
        if key in text:
            return val
    return command_all_default


def get_response(msg):
    func = get_command(msg)
    body = func(msg)
    if not body:
        return None
    is_at = msg['isAt']
    prefix = ''
    if is_at:
        prefix = u'@%s\u2005' % msg['ActualNickName']
    return prefix + body
