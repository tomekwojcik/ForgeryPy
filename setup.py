#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 by Tomasz Wójcik <labs@tomekwojcik.pl>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import codecs
import distutils.core

version = '0.1'

desc_file = codecs.open('README.rst', 'r', 'utf-8')
long_description = desc_file.read()
desc_file.close()

distutils.core.setup(
    name="ForgeryPy",
    version=version,
    packages=['forgery_py', 'forgery_py.forgery'],
    package_data={
        'forgery_py': [
            'dictionaries/cities',
            'dictionaries/colors',
            'dictionaries/company_names',
            'dictionaries/continents',
            'dictionaries/countries',
            'dictionaries/country_code_top_level_domains',
            'dictionaries/currency_codes',
            'dictionaries/currency_descriptions',
            'dictionaries/female_first_names',
            'dictionaries/frequencies',
            'dictionaries/genders',
            'dictionaries/industries',
            'dictionaries/job_title_suffixes',
            'dictionaries/job_titles',
            'dictionaries/languages',
            'dictionaries/last_names',
            'dictionaries/LICENSE',
            'dictionaries/locations',
            'dictionaries/lorem_ipsum',
            'dictionaries/male_first_names',
            'dictionaries/name_suffixes',
            'dictionaries/name_titles',
            'dictionaries/province_abbrevs',
            'dictionaries/provinces',
            'dictionaries/races',
            'dictionaries/shirt_sizes',
            'dictionaries/state_abbrevs',
            'dictionaries/states',
            'dictionaries/street_names',
            'dictionaries/street_suffixes',
            'dictionaries/top_level_domains',
            'dictionaries/zones'
        ]
    },
    author=u'Tomasz Wójcik',
    author_email='labs@tomekwojcik.pl',
    url='http://tomekwojcik.github.com/ForgeryPy/',
    download_url='http://github.com/tomekwojcik/ForgeryPy/tarball/v%s' % version,
    description='An easy to use forged data generator for Python',
    long_description=long_description,
    license='https://github.com/tomekwojcik/ForgeryPy/blob/master/LICENSE',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)