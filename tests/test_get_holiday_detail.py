# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import datetime
import unittest

from chinese_calendar import Holiday, get_holiday_detail


class GetHolidayDetailTests(unittest.TestCase):
    def test_holiday_in_english(self):
        national_day = datetime.date(2025, 10, 1)
        self.assertEqual((True, "National Day"), get_holiday_detail(national_day))
        self.assertEqual((True, Holiday.national_day.value), get_holiday_detail(national_day, in_english=True))

    def test_holiday_in_chinese(self):
        national_day = datetime.date(2025, 10, 1)
        self.assertEqual((True, "国庆节"), get_holiday_detail(national_day, in_english=False))

    def test_in_lieu_workday_in_chinese(self):
        # 2018-02-11 is a Sunday, but a workday in lieu of Spring Festival
        self.assertEqual((False, "春节"), get_holiday_detail(datetime.date(2018, 2, 11), in_english=False))

    def test_normal_day_in_chinese(self):
        self.assertEqual((True, None), get_holiday_detail(datetime.date(2018, 2, 10), in_english=False))
        self.assertEqual((False, None), get_holiday_detail(datetime.date(2018, 2, 12), in_english=False))
