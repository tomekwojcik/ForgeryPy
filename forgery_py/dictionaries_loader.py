# -*- coding: utf-8 -*-

import codecs
from os.path import abspath, dirname, join
import random

DICTIONARIES_PATH = abspath(join(dirname(__file__), 'dictionaries'))

dictionaries_cache = {}

def get_dictionary(dict_name):
    global dictionaries_cache

    if dict_name not in dictionaries_cache:
        try:
            dictionary_file = codecs.open(
                join(DICTIONARIES_PATH, dict_name), 'r', 'utf-8'
            )
        except IOError:
            None
        else:
            dictionaries_cache[dict_name] = dictionary_file.readlines()
            dictionary_file.close()

    return dictionaries_cache[dict_name]
