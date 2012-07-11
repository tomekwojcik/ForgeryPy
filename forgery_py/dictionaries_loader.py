# -*- coding: utf-8 -*-
"""File-based dictionaries support."""

import codecs
from os.path import abspath, dirname, join
import random

DICTIONARIES_PATH = abspath(join(dirname(__file__), 'dictionaries'))

dictionaries_cache = {}

def get_dictionary(dict_name):
    """
    Load a dictionary file ``dict_name`` (if it's not cached) and return its
    contents as an array of strings.
    """
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
