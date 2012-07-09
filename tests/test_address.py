# -*- coding: utf-8 -*-

import re
from unittest import TestCase

from forgery_py.forgery import address
from forgery_py.dictionaries_loader import get_dictionary


class AddressForgeryTestCase(TestCase):
    def test_street_name(self):
        result = address.street_name()
        assert result + '\n' in get_dictionary('street_names')

    def test_street_number(self):
        result = address.street_number()
        assert re.match(r'[0-9]{1,5}$', result) is not None

    def test_street_suffix(self):
        result = address.street_suffix()
        assert result + '\n' in get_dictionary('street_suffixes')

    def test_street_address(self):
        result = address.street_address()
        assert re.match(r'[0-9]{1,5} .+? .+?$', result)

    def test_city(self):
        result = address.city()
        assert result + '\n' in get_dictionary('cities')

    def test_state(self):
        result = address.state()
        assert result + '\n' in get_dictionary('states')

    def test_state_abbrev(self):
        result = address.state_abbrev()
        assert result + '\n' in get_dictionary('state_abbrevs')

    def test_zip_code(self):
        result = address.zip_code()
        assert (re.match(r'[0-9]{5}$', result) is not None or
                re.match(r'[0-9]{5}-[0-9]{4}$', result) is not None)

    def test_phone(self):
        result = address.phone()
        assert re.match(r'[0-9]-\([0-9]{3}\)[0-9]{3}-[0-9]{4}$', result) is not None

    def test_country(self):
        result = address.country()
        assert result + '\n' in get_dictionary('countries')

    def test_continent(self):
        result = address.continent()
        assert result + '\n' in get_dictionary('continents')
