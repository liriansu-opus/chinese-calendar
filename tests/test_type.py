# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import datetime
import time
import unittest

import chinese_calendar


class TypeTests(unittest.TestCase):
    def test_date(self):
        date = datetime.date.today()
        chinese_calendar.is_holiday(date)
        self.assertTrue(True)

    def test_datetime(self):
        date = datetime.datetime.today()
        chinese_calendar.is_holiday(date)
        self.assertTrue(True)

    def test_wrong_type(self):
        date = time.time()
        with self.assertRaises(NotImplementedError):
            # noinspection PyTypeChecker
            chinese_calendar.is_holiday(date)  # NOQA
