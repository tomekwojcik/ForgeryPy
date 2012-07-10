# -*- coding: utf-8 -*-

import random
import string

from ..dictionaries_loader import get_dictionary

__all__ = [
    'street_name', 'street_number', 'street_suffix', 'street_address',
    'city', 'state', 'state_abbrev', 'zip_code', 'phone', 'country', 'continent'
]

def street_name():
    return random.choice(get_dictionary('street_names')).strip()

def street_number():
    length = int(random.choice(string.digits[1:6]))
    return ''.join(random.sample(string.digits, length))

def street_suffix():
    return random.choice(get_dictionary('street_suffixes')).strip()

def street_address():
    return '%s %s %s' % (street_number(), street_name(), street_suffix())

def city():
    return random.choice(get_dictionary('cities')).strip()

def state():
    return random.choice(get_dictionary('states')).strip()

def state_abbrev():
    return random.choice(get_dictionary('state_abbrevs')).strip()

def zip_code():
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
    format = '#-(###)###-####'

    result = ''
    for item in format:
        if item == '#':
            result += str(random.randint(0, 9))
        else:
            result += item

    return result

def country():
    return random.choice(get_dictionary('countries')).strip()

def continent():
    return random.choice(get_dictionary('continents')).strip()
