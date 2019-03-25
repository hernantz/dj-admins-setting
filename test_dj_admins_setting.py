#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

import dj_admins_setting


class AdminTestSuite(unittest.TestCase):
    def test_admins_email_env_parsing(self):
        a = dj_admins_setting.config()
        assert not a

        os.environ['ADMINS'] = '"Firstname Lastname" <email@example.com>'

        a = dj_admins_setting.config()

        assert a == [('Firstname Lastname', 'email@example.com')]

    def test_admins_email_parsing(self):
        a = dj_admins_setting.parse('"Firstname Lastname" <email@example.com>')
        assert a == [('Firstname Lastname', 'email@example.com')]

        a = dj_admins_setting.parse('"Firstname Lastname" <email@example.com>,'
                                    ' "Another Name" <another@example.com')
        assert a == [
            ('Firstname Lastname', 'email@example.com'),
            ('Another Name', 'another@example.com')
        ]

        a = dj_admins_setting.parse('"Firstname Lastname" <email@example.com>,'
                                    ' another@example.com')
        assert a == [
            ('Firstname Lastname', 'email@example.com'),
            ('', 'another@example.com')
        ]

        a = dj_admins_setting.parse('email@example.com, another@example.com')
        assert a == [
            ('', 'email@example.com'),
            ('', 'another@example.com')
        ]


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
