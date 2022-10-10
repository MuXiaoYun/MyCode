import unittest

from app.checkers.user import register_params_check


class BasicTestCase(unittest.TestCase):
    '''
    TODO: 在这里补充注册相关测试用例
    '''

    def test_register_params_check(self):
        def user_content(username, password, mobile, url, nickname, magic_number = 0):
            return {
                "username": username,
                "password": password,
                "mobile": mobile,
                "url": url,
                "nickname": nickname,
                "magic_number": magic_number
            }

        c1 = user_content(
            'HeMu123',
            'AB123cd*_a',
            '+86.113685569120',
            'https://www.baidu.com',
            'sleepgary',
            7)
        # 全部合规
        c2 = user_content(
            None,
            'AB123cd*_a',
            '+86.113685569120',
            'https://www.baidu.com',
            'sleepgary',
            7)
        # 用户名缺失
        c3 = user_content(
            'HeMu123333333333333333333',
            'AB123cd*_a',
            '+86.113685569120',
            'https://www.baidu.com',
            'sleepgary',
            7)
        # 用户名长度过长
        c4 = user_content(
            'He1Mu123',
            'AB123cd*_a',
            '+86.113685569120',
            'https://www.baidu.com',
            'sleepgary',
            7)
        # 用户名字母数字顺序不正确
        c5 = user_content(
            'HeMu123',
            'AB123333333333333333333cd*_a',
            '+86.113685569120',
            'https://www.baidu.com',
            'sleepgary',
            7)
        # 密码过长
        c6 = user_content(
            'HeMu123',
            'AB123233*_',
            '+86.113685569120',
            'https://www.baidu.com',
            'sleepgary',
            7)
        # 密码没有小写字母
        c7 = user_content(
            'HeMu123',
            'ABplace*_a',
            '+86.113685569120',
            'https://www.baidu.com',
            'sleepgary',
            7)
        # 密码没有数字
        c8 = user_content(
            'HeMu123',
            'ab123cd*_a',
            '+86.113685569120',
            'https://www.baidu.com',
            'sleepgary',
            7)
        # 密码没有大写字母
        c9 = user_content(
            'HeMu123',
            'AB123cdnda',
            '+86.113685569120',
            'https://www.baidu.com',
            'sleepgary',
            7)
        # 密码没有符号
        c10 = user_content(
            'HeMu123',
            'AB123cd*_a',
            '113685569120',
            'https://www.baidu.com',
            'sleepgary',
            7)
        # 手机号不符合格式
        c11 = user_content(
            'HeMu123',
            'AB123cd*_a',
            '+86.113685569120',
            'www.baidu.com',
            'sleepgary',
            7)
        # 域名头不对
        c12 = user_content(
            'HeMu123',
            'AB123cd*_a',
            '+86.113685569120',
            'https://www.baidu.com.126',
            'sleepgary',
            7)
        # 末尾是纯数字
        c13 = user_content(
            'HeMu123',
            'AB123cd*_a',
            '+86.113685569120',
            'https://www.baidu.com.12-',
            'sleepgary',
            7)
        # 连字符位置在最末
        c14 = user_content(
            'HeMu123',
            'AB123cd*_a',
            '+86.113685569120',
            'https://www.baidu.com-.12a',
            'sleepgary',
            7)
        # 连字符位置在某标签末尾
        c15 = user_content(
            'HeMu123',
            'AB123cd*_a',
            '+86.113685569120',
            'https://www.baidu.-com.12a',
            'sleepgary',
            7)
        # 连字符位置在某标签开头
        c16 = user_content(
            'HeMu123',
            'AB123cd*_a',
            '+86.113685569120',
            'https://www.baidu.com',
            'sleepgary')
        # 没有输入幸运数字
        c17 = user_content('HeMu123', 'AB123cd*_a', '+86.113685569120',
                           'https://www.baidu.com', 'sleepgary', -1)
        # 幸运数字是负数
        c18 = user_content(
            'HeMu123',
            'AB123cd*_a',
            '+86.113685569120',
            'https://www.baidu.com',
            'sleepgary',
            1.2)
        # 幸运数字是浮点数
        c19 = user_content(
            'HeMu123',
            None,
            '+86.113685569120',
            'https://www.baidu.com',
            'sleepgary',
            1)
        # 没有密码
        c20 = user_content(
            'HeMu123',
            'AB123cd*_a',
            None,
            'https://www.baidu.com',
            'sleepgary',
            1)
        # 没有电话
        c21 = user_content(
            'HeMu123',
            'AB123cd*_a',
            '+86.113685569120',
            None,
            'sleepgary',
            1)
        # 没有网址
        c22 = user_content(
            'HeMu123',
            'AB123cd*_a',
            '+86.113685569120',
            'https://www.baidu.com',
            None,
            1)
        # 没有昵称
        self.assertEqual(register_params_check(c1), ("ok", True))
        self.assertEqual(register_params_check(c2), ("username", False))
        self.assertEqual(register_params_check(c3), ("username", False))
        self.assertEqual(register_params_check(c4), ("username", False))
        self.assertEqual(register_params_check(c5), ("password", False))
        self.assertEqual(register_params_check(c6), ("password", False))
        self.assertEqual(register_params_check(c7), ("password", False))
        self.assertEqual(register_params_check(c8), ("password", False))
        self.assertEqual(register_params_check(c9), ("password", False))
        self.assertEqual(register_params_check(c10), ("mobile", False))
        self.assertEqual(register_params_check(c11), ("url", False))
        self.assertEqual(register_params_check(c12), ("url", False))
        self.assertEqual(register_params_check(c13), ("url", False))
        self.assertEqual(register_params_check(c14), ("url", False))
        self.assertEqual(register_params_check(c15), ("url", False))
        self.assertEqual(register_params_check(c16), ("ok", True))
        self.assertEqual(register_params_check(c17), ("magic_number", False))
        self.assertEqual(register_params_check(c18), ("magic_number", False))
        self.assertEqual(register_params_check(c19), ("password", False))
        self.assertEqual(register_params_check(c20), ("mobile", False))
        self.assertEqual(register_params_check(c21), ("url", False))
        self.assertEqual(register_params_check(c22), ("nickname", False))


if __name__ == '__main__':
    unittest.main()
