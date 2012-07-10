# -*- coding: utf-8 -*-

import datetime
from unittest import TestCase

from forgery_py.forgery import date


class DateForgeryTestCase(TestCase):
    def test_day_of_week(self):
        result = date.day_of_week()
        assert result in date.DAYS

        result = date.day_of_week(abbr=True)
        assert result in date.DAYS_ABBR

    def test_month(self):
        result = date.month()
        assert result in date.MONTHS

        result = date.month(abbr=True)
        assert result in date.MONTHS_ABBR

        result = date.month(numerical=True)
        assert result in range(1, 13)

    def test_year(self):
        today = datetime.date.today()

        result = date.year()
        assert result > today.year

        result = date.year(past=True)
        assert result < today.year

    def test_day(self):
        result = date.day()
        assert result in range(1, 32)

        result = date.day(2)
        assert result in range(1, 3)

    def test_date(self):
        today = datetime.date.today()

        result = date.date()
        assert result > today

        result = date.date(past=True)
        assert result < today