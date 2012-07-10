# -*- coding: utf-8 -*-

import random

from ..dictionaries_loader import get_dictionary

__all__ = []


def description():
    return random.choice(get_dictionary('currency_descriptions')).strip()


def code():
    return random.choice(get_dictionary('currency_codes')).strip()
