# -*- coding: utf-8 -*-
"""Generate forged addres-related data."""

import random
import string

from ..dictionaries_loader import get_dictionary

__all__ = [
    'street_name', 'street_number', 'street_suffix', 'street_address',
    'city', 'state', 'state_abbrev', 'zip_code', 'phone', 'country', 'continent'
]

def street_name():
    """Random street name."""
    return random.choice(get_dictionary('street_names')).strip()

def street_number():
    """Random street number."""
    length = int(random.choice(string.digits[1:6]))
    return ''.join(random.sample(string.digits, length))

def street_suffix():
    """Random street suffix."""
    return random.choice(get_dictionary('street_suffixes')).strip()

def street_address():
    """
    Random street address. Equivalent of ``street_number() + ' ' + 
    street_name() + ' ' + street_suffix()``.
    """
    return '%s %s %s' % (street_number(), street_name(), street_suffix())

def city():
    """Random city name."""
    return random.choice(get_dictionary('cities')).strip()

def state():
    """Random US state name."""
    return random.choice(get_dictionary('states')).strip()

def state_abbrev():
    """Random US abbreviated state name."""
    return random.choice(get_dictionary('state_abbrevs')).strip()

def zip_code():
    """Random ZIP code, either in `#####` or `#####-####` format."""
    format = '#####'
    if random.random() >= 0.5:
        format = '#####-####'

    result = ''
    for item in format:
        if item == '#':
            result += str(random.randint(0, 9))
        else:
            result += item

    return result

def phone():
    """Random phone number in `#-(###)###-####` format."""
    format = '#-(###)###-####'

    result = ''
    for item in format:
        if item == '#':
            result += str(random.randint(0, 9))
        else:
            result += item

    return result

def country():
    """Random country name."""
    return random.choice(get_dictionary('countries')).strip()

def continent():
    """Random continent name."""
    return random.choice(get_dictionary('continents')).strip()
