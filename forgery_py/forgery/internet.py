# -*- coding: utf-8 -*-

import random

from ..dictionaries_loader import get_dictionary
from .name import first_name

__all__ = [
    'user_name', 'top_level_domain', 'domain_name',
    'email_address', 'cctld', 'ip_v4'
]


def user_name(with_num=False):
    result = first_name()
    if with_num:
        result += str(random.randint(63, 94))

    return result.lower()

def top_level_domain():
    return random.choice(get_dictionary('top_level_domains')).strip()

def domain_name():
    result = random.choice(get_dictionary('company_names')).strip()
    result += '.' + top_level_domain()

    return result.lower()

def email_address(user=None):
    if not user:
        user = user_name()
    else:
        user = user.strip().replace(' ', '_').lower()

    return user + '@' + domain_name()

def cctld():
    return random.choice(get_dictionary('country_code_top_level_domains')).\
        strip()

def ip_v4():
    return '.'.join([str(random.randint(0, 255)) for i in xrange(0, 4)])
