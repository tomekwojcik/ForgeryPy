# -*- coding: utf-8 -*-
"""Generate random date-related data."""

import datetime
import random

from ..dictionaries_loader import get_dictionary

__all__ = ['day_of_week', 'month', 'year', 'day', 'date']

DAYS = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday',
    'Friday', 'Saturday', 'Sunday'
]

DAYS_ABBR = [
    'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'
]

MONTHS = [
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]

MONTHS_ABBR = [
    'Jan', 'Feb', 'Mar', 'Apr',
    'May', 'Jun', 'Jul', 'Aug',
    'Sep', 'Oct', 'Nov', 'Dec'
]


def day_of_week(abbr=False):
    """Random (abbreviated if `abbr`) day of week name."""
    if abbr:
        return random.choice(DAYS_ABBR)
    else:
        return random.choice(DAYS)


def month(abbr=False, numerical=False):
    """
    Random (abbreviated if `abbr`) month name or month number if 
    `numerical`.
    """
    if numerical:
        return random.randint(1, 12)
    else:
        if abbr:
            return random.choice(MONTHS_ABBR)
        else:
            return random.choice(MONTHS)


def _delta(past=False, min_delta=0, max_delta=20):
    delta = min_delta + random.randint(min_delta + 1, max_delta)

    if past:
        delta = delta * -1

    return delta


def year(past=False, min_delta=0, max_delta=20):
    """Random year."""
    return datetime.date.today().year + _delta(past, min_delta, max_delta)


def day(month_length=31):
    """Random day number in a `month_length` days long month."""
    return random.randint(1, month_length)


def date(past=False, min_delta=0, max_delta=20):
    """Random `datetime.date` object. Delta args are days."""
    timedelta = datetime.timedelta(days=_delta(past, min_delta, max_delta))
    return datetime.date.today() + timedelta