# -*- coding: utf-8 -*-
import unittest

import chinese_calendar


class InLieuTests(unittest.TestCase):
    def test_in_lieu_should_be_holiday(self):
        self.assertTrue(all(chinese_calendar.is_holiday(_) for _ in chinese_calendar.in_lieu_days))

    def test_in_lieu_should_equal_workdays_amount(self):
        min_year, max_year = min(chinese_calendar.in_lieu_days.keys()).year, max(chinese_calendar.holidays.keys()).year
        for year in range(min_year, max_year + 1):
            in_lieu_days_amount = len(
                list(filter(lambda date: date.year == year, chinese_calendar.in_lieu_days.keys()))
            )
            workdays_amount = len(list(filter(lambda date: date.year == year, chinese_calendar.workdays.keys())))
            if year == 2006:
                in_lieu_days_amount += 2  # 06年要补班07年的元旦假期
            elif year == 2007:
                workdays_amount += 2  # 07年可以享受06年补班的假
            elif year == 2011:
                in_lieu_days_amount += 1  # 11年要补班12年的元旦假期
            elif year == 2012:
                workdays_amount += 1  # 12年可以享受11年补班的假
            elif year == 2018:
                workdays_amount += 1  # 19年元旦多享受一天假期
            self.assertEqual(in_lieu_days_amount, workdays_amount, "year {}".format(year))

    def test_in_lieu_should_be_weekday(self):
        for in_lieu_day in chinese_calendar.in_lieu_days.keys():
            self.assertLess(in_lieu_day.weekday(), 5, str(in_lieu_day))
