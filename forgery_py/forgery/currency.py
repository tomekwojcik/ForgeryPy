# -*- coding: utf-8 -*-
"""Generate currency-related data."""

import random

from ..dictionaries_loader import get_dictionary

__all__ = ['description', 'code']


def description():
    """Random currency description, e.g. `United Kingdom Pounds`."""
    return random.choice(get_dictionary('currency_descriptions')).strip()


def code():
    """Random currency code, e.g. `GBP`."""
    return random.choice(get_dictionary('currency_codes')).strip()
