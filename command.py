# coding=utf8
command_map_at = {}
command_map_all = {}
command_at_default = None
command_all_default = None


def set_command(keys, is_at, is_default, func):
    global command_at_default, command_all_default
    if is_default:
        if is_at:
            command_at_default = func
        else:
            command_all_default = func
    elif is_at:
        for idx in range(len(keys)):
            command_map_at[keys[idx]] = func
    else:
        for idx in range(len(keys)):
            command_map_all[keys[idx]] = func


def get_command(msg):
    text = msg['Text']
    is_at = msg['isAt']
    if is_at:
        for key in command_map_at.keys():
            if key in text:
                return command_map_at[key]
        return command_at_default
    for key in command_map_all.keys():
        if key in text:
            return command_map_all[key]
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
