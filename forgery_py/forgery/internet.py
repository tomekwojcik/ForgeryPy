# -*- coding: utf-8 -*-

import random

from ..dictionaries_loader import get_dictionary

__all__ = [
    'user_name', 'top_level_domain', 'domain_name',
    'email_address', 'cctld', 'ip_v4'
]


def user_name(sex=None, with_num=False):
    if sex not in ['male', 'female']:
        sex = None

    if not sex:
        if random.random() > 0.5:
            sex = 'male'
        else:
            sex = 'female'

    result = random.choice(get_dictionary(sex + '_first_names')).strip()
    if with_num:
        result += str(random.randint(63, 94))

    return result.lower()

def top_level_domain():
    return random.choice(get_dictionary('top_level_domains')).strip()

def domain_name():
    result = random.choice(get_dictionary('company_names')).strip()
    result += '.' + top_level_domain()

    return result.lower()

def email_address():
    return user_name() + '@' + domain_name()

def cctld():
    return random.choice(get_dictionary('country_code_top_level_domains')).\
        strip()

def ip_v4():
    return '.'.join([str(random.randint(0, 256)) for i in xrange(0, 4)])
