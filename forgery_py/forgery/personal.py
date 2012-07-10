# -*- coding: utf-8 -*-

import random

from ..dictionaries_loader import get_dictionary

__all__ = ['gender', 'abbreviated_gender', 'shirt_size', 'race', 'language']


def gender():
    return random.choice(get_dictionary('genders')).strip()


def abbreviated_gender():
    return gender()[0:1]


def shirt_size():
    return random.choice(get_dictionary('shirt_sizes')).strip()


def race():
    return random.choice(get_dictionary('races')).strip()


def language():
    return random.choice(get_dictionary('languages')).strip()