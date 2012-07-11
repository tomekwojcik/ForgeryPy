# -*- coding: utf-8 -*-
"""Generate misc random data."""

import random
import string

HEX_DIGITS = string.hexdigits[:-6].upper()

__all__ = ['hex_color', 'hex_color_short', 'text']


def hex_color():
    """Random HEX color."""
    return ''.join(random.sample(HEX_DIGITS, 6))

def hex_color_short():
    """Random short (e.g. `FFF` color)."""
    return ''.join(random.sample(HEX_DIGITS, 3))

def text(length=None, at_least=10, at_most=15, lowercase=True,
         uppercase=True, digits=True, spaces=True, punctuation=False):
    """
    Random text.

    If `length` is present the text will be exactly this chars long. Else the
    text will be something between `at_least` and `at_most` chars long.
    """
    base_string = ''
    if lowercase:
        base_string += string.ascii_lowercase

    if uppercase:
        base_string += string.ascii_uppercase

    if digits:
        base_string += string.digits

    if spaces:
        base_string += ' '

    if punctuation:
        base_string += string.punctuation

    if len(base_string) == 0:
        return ''

    if not length:
        length = random.randint(at_least, at_most)

    result = ''
    for i in xrange(0, length):
        result += random.choice(base_string)

    return result
