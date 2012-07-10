# -*- coding: utf-8 -*-

import random

from ..dictionaries_loader import get_dictionary

__all__ = [
    'first_name', 'last_name', 'full_name', 'male_first_name',
    'female_first_name', 'company_name', 'job_title', 'job_title_suffix',
    'title', 'suffix', 'location', 'industry'
]


def first_name():
    _dict = get_dictionary('male_first_names')
    _dict += get_dictionary('female_first_names')

    return random.choice(_dict).strip()


def last_name():
    return random.choice(get_dictionary('last_names')).strip()


def full_name():
    return first_name() + ' ' + last_name()


def male_first_name():
    return random.choice(get_dictionary('male_first_names')).strip()


def female_first_name():
    return random.choice(get_dictionary('female_first_names')).strip()


def company_name():
    return random.choice(get_dictionary('company_names')).strip()


def job_title():
    result = random.choice(get_dictionary('job_titles')).strip()
    result = result.replace('#{N}', job_title_suffix())
    return result

def job_title_suffix():
    return random.choice(get_dictionary('job_title_suffixes')).strip()


def title():
    return random.choice(get_dictionary('name_titles')).strip()


def suffix():
    return random.choice(get_dictionary('name_suffixes')).strip()


def location():
    return random.choice(get_dictionary('locations')).strip()


def industry():
    return random.choice(get_dictionary('industries')).strip()