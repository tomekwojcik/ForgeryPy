# -*- coding: utf-8 -*-

from unittest import TestCase

from forgery_py.forgery import name
from forgery_py.dictionaries_loader import get_dictionary


class NameForgeryTestCase(TestCase):
    def test_first_name(self):
        result = name.first_name()
        assert result + '\n' in get_dictionary('male_first_names') or\
            result + '\n' in get_dictionary('female_first_names')

        result = name.male_first_name()
        assert result + '\n' in get_dictionary('male_first_names')

        result = name.female_first_name()
        assert result + '\n' in get_dictionary('female_first_names')

    def test_last_name(self):
        result = name.last_name()
        assert result + '\n' in get_dictionary('last_names')

    def test_full_name(self):
        result = name.full_name()

        assert len(result.split(' ')) == 2

    def test_company_name(self):
        result = name.company_name()
        assert result + '\n' in get_dictionary('company_names')

    def test_job_title_suffix(self):
        result = name.job_title_suffix()
        assert result + '\n' in get_dictionary('job_title_suffixes')

    def test_title(self):
        result = name.title()
        assert result + '\n' in get_dictionary('name_titles')

    def test_suffix(self):
        result = name.suffix()
        assert result + '\n' in get_dictionary('name_suffixes')

    def test_location(self):
        result = name.location()
        assert result + '\n' in get_dictionary('locations')

    def test_industry(self):
        result = name.industry()
        assert result + '\n' in get_dictionary('industries')