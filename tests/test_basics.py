# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import datetime
import unittest

from chinese_calendar import Holiday, get_holiday_detail, is_holiday, is_workday


class BasicTests(unittest.TestCase):
    def test_opposite(self):
        date = datetime.date.today()
        self.assertEqual(not is_workday(date), is_holiday(date))

    def test_holidays(self):
        dates = [
            datetime.date(year=2017, month=5, day=30),
            datetime.date(year=2017, month=6, day=4),
            datetime.date(year=2017, month=10, day=1),
            datetime.date(year=2018, month=5, day=1),
        ]
        for date in dates:
            self.assertFalse(is_workday(date))
            self.assertTrue(is_holiday(date))

    def test_workdays(self):
        dates = [
            datetime.date(year=2017, month=5, day=27),
            datetime.date(year=2017, month=6, day=5),
            datetime.date(year=2017, month=10, day=31),
            datetime.date(year=2018, month=5, day=10),
        ]
        for date in dates:
            self.assertFalse(is_holiday(date))
            self.assertTrue(is_workday(date))

    def test_detail(self):
        cases = [
            ((2018, 2, 10), (True, None)),
            ((2018, 2, 11), (False, Holiday.spring_festival.value)),
            ((2018, 2, 12), (False, None)),
            ((2018, 2, 15), (True, Holiday.spring_festival.value)),
        ]
        for date, expected_result in cases:
            self.assertEqual(expected_result, get_holiday_detail(datetime.date(*date)))

    def test_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            is_holiday(datetime.date(year=2001, month=1, day=1))
