# -*- coding: utf-8 -*-

from unittest import TestCase

from forgery_py.forgery import personal
from forgery_py.dictionaries_loader import get_dictionary


class PersonalForgeryTestCase(TestCase):
    def test_gender(self):
        result = personal.gender()
        assert result + '\n' in get_dictionary('genders')

        result = personal.abbreviated_gender()
        assert result in ('M', 'F')

    def test_shirt_size(self):
        result = personal.shirt_size()
        assert result + '\n' in get_dictionary('shirt_sizes')

    def test_race(self):
        result = personal.race()
        assert result + '\n' in get_dictionary('races')

    def test_language(self):
        result = personal.language()
        assert result + '\n' in get_dictionary('languages')
