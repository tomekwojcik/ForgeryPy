# -*- coding: utf-8 -*-

import re
from unittest import TestCase

from forgery_py.forgery import currency
from forgery_py.dictionaries_loader import get_dictionary


class CurrencyForgeryTestCase(TestCase):
    def test_description(self):
        result = currency.description()
        assert result + '\n' in get_dictionary('currency_descriptions')

    def test_code(self):
        result = currency.code()
        assert result + '\n' in get_dictionary('currency_codes')