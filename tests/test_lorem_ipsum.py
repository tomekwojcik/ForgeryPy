# -*- coding: utf-8 -*-

import re
import string
from unittest import TestCase

from forgery_py.forgery import lorem_ipsum


class LoremIpsumForgeryTestCase(TestCase):
    def test_word(self):
        result = lorem_ipsum.word()
        assert re.match(r'[a-z]+?$', result) is not None

    def test_words(self):
        result = lorem_ipsum.words(5)
        assert len(result.split(' ')) == 5

        result = lorem_ipsum.words(5, as_list=True)
        assert len(result) == 5

    def test_title(self):
        result = lorem_ipsum.title()
        assert result[0] in string.ascii_uppercase
        assert len(result.split(' ')) == 4
        assert result[-1] in ('?.!')

    def test_sentence(self):
        result = lorem_ipsum.sentence()
        assert len(result.split('.')) == 2

    def test_sentences(self):
        result = lorem_ipsum.sentences()
        assert len(result.split('.')) == 3

    def test_paragraph(self):
        result = lorem_ipsum.paragraph()
        assert len(result.split('.')) == 4

    def test_paragraphs(self):
        result = lorem_ipsum.paragraphs(separator='|')
        assert len(result.split('|')) == 2

        result = lorem_ipsum.paragraphs(as_list=True)
        assert len(result) == 2

        result = lorem_ipsum.paragraphs(html=True, as_list=True)

        for paragraph in result:
            assert paragraph.startswith('<p>')
            assert paragraph.endswith('</p>')