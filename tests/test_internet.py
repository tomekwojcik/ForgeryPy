# -*- coding: utf-8 -*-

import re
import string
from unittest import TestCase

from forgery_py.forgery import internet
from forgery_py.dictionaries_loader import get_dictionary


class InternetForgeryTestCase(TestCase):
    def test_user_name(self):
        result = internet.user_name(sex='male')
        assert re.match(r'[a-z]+?$', result) is not None
        assert result.capitalize() + '\n'\
            in get_dictionary('male_first_names')

        result = internet.user_name(sex='female')
        assert result.capitalize() + '\n'\
            in get_dictionary('female_first_names')

        result = internet.user_name(with_num=True)
        assert int(result[-2:]) in range(63, 95)

    def test_top_level_domain(self):
        result = internet.top_level_domain()
        assert result + '\n' in get_dictionary('top_level_domains')

    def test_domain_name(self):
        result = internet.domain_name()
        print result
        assert re.match(r'[a-z]+?\.[a-z]{3,4}$', result) is not None

    def test_email_address(self):
        result = internet.email_address()
        assert re.match(r'[a-z]+?@[a-z]+?\.[a-z]{3,4}$', result) is not None

    def test_ccld(self):
        result = internet.cctld()
        assert result + '\n'\
            in get_dictionary('country_code_top_level_domains')

    def test_ip_v4(self):
        result = internet.ip_v4().split('.')
        assert len(result) == 4

        for block in result:
            assert int(block) in range(0, 256)
