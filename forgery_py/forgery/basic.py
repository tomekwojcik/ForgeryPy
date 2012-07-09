# -*- coding: utf-8 -*-

import random
import string

HEX_DIGITS = string.hexdigits[:-6].upper()

__all__ = ['BasicForgeryMixin']


class BasicForgeryMixin(object):
    def hex_color(self):
        return ''.join(random.sample(HEX_DIGITS, 6))

    def hex_color_short(self):
        return ''.join(random.sample(HEX_DIGITS, 3))

    def text(self, length=None, at_least=10, at_most=15, lowercase=True,
             uppercase=True, digits=True, spaces=True, punctuation=False):
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
