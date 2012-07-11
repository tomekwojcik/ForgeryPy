# -*- coding: utf-8 -*-
"""Generate random personal information."""

import random

from ..dictionaries_loader import get_dictionary

__all__ = ['gender', 'abbreviated_gender', 'shirt_size', 'race', 'language']


def gender():
    """Random gender."""
    return random.choice(get_dictionary('genders')).strip()


def abbreviated_gender():
    """Random abbreviated gender."""
    return gender()[0:1]


def shirt_size():
    """Shirt size."""
    return random.choice(get_dictionary('shirt_sizes')).strip()


def race():
    """Random race."""
    return random.choice(get_dictionary('races')).strip()


def language():
    """Random language name, e.g. ``Polish``."""
    return random.choice(get_dictionary('languages')).strip()