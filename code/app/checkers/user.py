# -*- coding: utf-8 -*-

def register_params_check(content: 'dict'):
    """
    TODO: 进行参数检查
    """
    if not content['username']:
        return 'username', False
    if not content['password']:
        return 'password', False
    if not content['url']:
        return 'url', False
    if not content['nickname']:
        return 'nickname', False
    if not content['mobile']:
        return 'mobile', False
    if not content['magic_number']:
        content['magic_number'] = 0

    import re
    if re.match(
        r'^[A-Za-z0-9]{5,12}$',
        content['username']) is None or re.match(
        r'^[A-Za-z]+[\d]+$',
            content['username']) is None:
        return 'username', False
    if re.match(
            r'^[A-Z a-z 0-9 \- \* \^ _]{8,15}$',
            content['password']) is None or not re.match(
            r'^[a-z 0-9 \- \* \^ _]{8,15}$',
            content['password']) is None or not re.match(
                r'^[A-Z 0-9 \- \* \^ _]{8,15}$',
                content['password']) is None or not re.match(
                    r'^[A-Z a-z \- \* \^ _]{8,15}$',
                    content['password']) is None or not re.match(
                        r'^[A-Z a-z 0-9]{8,15}$',
            content['password']) is None:
        return 'password', False
    if re.match(r'^\+\d{2}\.\d{12}$', content['mobile']) is None:
        return 'mobile', False
    if re.match(
            r'^https?://[A-Za-z0-9\-\.]{1,48}$',
            content['url']) is None or re.match(
            r'^https?://([A-Za-z0-9\-]+\.)+[A-Za-z0-9\-]+$',
            content['url']) is None or not re.match(
                r'^https?://([A-Za-z0-9\-]+\.)+[0-9]+$',
            content['url']) is None:
        # 第一个正则表达式用于限定长度
        # 第二个正则表达式用于限定标签序列格式
        # 第三个正则表达式用于限定末尾不是纯数字
        return 'url', False
    if not re.search(
            r'\-\.',
            content['url']) is None or not re.search(
            r'\.\-',
            content['url']) is None or not re.search(
                r'\-$',
            content['url']) is None:
        return 'url', False
        # 限定连字符位置
    if content['magic_number'] < 0 or not isinstance(content['magic_number'], int):
        return 'magic_number', False
    return "ok", True
