# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import datetime

from chinese_calendar.constants import Holiday, holidays, in_lieu_days, workdays
from chinese_calendar.solar_terms import (
    SOLAR_TERMS_C_NUMS,
    SOLAR_TERMS_DELTA,
    SOLAR_TERMS_MONTH,
    SolarTerms,
)


def _wrap_date(date):
    """
    transform datetime.datetime into datetime.date

    :type date: datetime.date | datetime.datetime
    :rtype: datetime.date
    """
    if isinstance(date, datetime.datetime):
        date = date.date()
    return date


def _validate_date(*dates):
    """
    check if the date(s) is supported

    :type date: datetime.date | datetime.datetime
    :rtype: datetime.date | list[datetime.date]
    """
    if len(dates) != 1:
        return list(map(_validate_date, dates))
    date = _wrap_date(dates[0])
    if not isinstance(date, datetime.date):
        raise NotImplementedError("unsupported type {}, expected type is datetime.date".format(type(date)))
    min_year, max_year = min(holidays.keys()).year, max(holidays.keys()).year
    if not (min_year <= date.year <= max_year):
        raise NotImplementedError(
            "no available data for year {}, only year between [{}, {}] supported".format(date.year, min_year, max_year)
        )
    return date


def is_holiday(date):
    """
    check if one date is holiday in China.
    in other words, Chinese people get rest at that day.

    :type date: datetime.date | datetime.datetime
    :rtype: bool
    """
    return not is_workday(date)


def is_workday(date):
    """
    check if one date is workday in China.
    in other words, Chinese people works at that day.

    :type date: datetime.date | datetime.datetime
    :rtype: bool
    """
    date = _validate_date(date)

    weekday = date.weekday()
    return bool(date in workdays.keys() or (weekday <= 4 and date not in holidays.keys()))


def is_in_lieu(date):
    """
    check if one date is in lieu in China.
    in other words, Chinese people get rest at that day because of legal holiday.

    :type date: datetime.date | datetime.datetime
    :rtype: bool
    """
    date = _validate_date(date)

    return date in in_lieu_days


def get_holiday_detail(date, in_english=True):
    """
    check if one date is holiday in China,
    and return the holiday name (None if it's a normal day)

    :type date: datetime.date | datetime.datetime
    :param in_english: return the English holiday name if True, otherwise the Chinese one
    :type in_english: bool
    :return: holiday bool indicator, and holiday name if it's holiday related day
    :rtype: (bool, str | None)
    """
    date = _validate_date(date)
    if date in workdays.keys():
        on_holiday, name = False, workdays[date]
    elif date in holidays.keys():
        on_holiday, name = True, holidays[date]
    else:
        return date.weekday() > 4, None
    return on_holiday, name if in_english else Holiday(name).chinese


def get_dates(start, end):
    """
    get dates between start date and end date. (includes start date and end date)

    :type start: datetime.date | datetime.datetime
    :type end:  datetime.date | datetime.datetime
    :rtype: list[datetime.date]
    """
    start, end = map(_wrap_date, (start, end))
    delta_days = (end - start).days
    return [start + datetime.timedelta(days=delta) for delta in range(delta_days + 1)]


def get_holidays(start, end, include_weekends=True):
    """
    get holidays between start date and end date. (includes start date and end date)

    :type start: datetime.date | datetime.datetime
    :type end:  datetime.date | datetime.datetime
    :type include_weekends: bool
    :param include_weekends: False for excluding Saturdays and Sundays
    :rtype: list[datetime.date]
    """
    start, end = _validate_date(start, end)
    if include_weekends:
        return list(filter(is_holiday, get_dates(start, end)))
    return list(filter(lambda x: x in holidays, get_dates(start, end)))


def get_workdays(start, end, include_weekends=True):
    """
    get workdays between start date and end date. (includes start date and end date)

    :type start: datetime.date | datetime.datetime
    :type end:  datetime.date | datetime.datetime
    :type include_weekends: bool
    :param include_weekends: False for excluding Saturdays and Sundays
    :rtype: list[datetime.date]
    """
    start, end = _validate_date(start, end)
    if include_weekends:
        return list(filter(is_workday, get_dates(start, end)))
    return list(filter(lambda x: is_workday(x) and x.weekday() < 5, get_dates(start, end)))


def find_workday(delta_days=0, date=None):
    """
    find the workday after {delta_days} days.

    :type delta_days: int
    :param delta_days: 0 means next workday (includes today), -1 means previous workday.
    :type date: datetime.date | datetime.datetime
    :param: the start point
    :rtype: datetime.date
    """
    date = _wrap_date(date or datetime.date.today())
    if delta_days >= 0:
        delta_days += 1
    sign = 1 if delta_days >= 0 else -1
    for i in range(abs(delta_days)):
        if delta_days < 0 or i:
            date += datetime.timedelta(days=sign)
        while not is_workday(date):
            date += datetime.timedelta(days=sign)
    return date


def get_solar_terms(start, end):
    """
    生成 24 节气
    通用寿星公式： https://www.jianshu.com/p/1f814c6bb475

    通式寿星公式：[Y×D+C]-L
    []里面取整数； Y=年数的后2位数； D=0.2422； L=Y/4，小寒、大寒、立春、雨水的 L=(Y-1)/4

    :type start: datetime.date
    :param start: 开始日期
    :type end: datetime.date
    :param end: 结束日期
    :rtype: list[(datetime.date, str)]
    """
    if not 1900 <= start.year <= 2100 or not 1900 <= end.year <= 2100:
        raise NotImplementedError("only year between [1900, 2100] supported")
    D = 0.2422
    result = []
    year, month = start.year, start.month
    while year < end.year or (year == end.year and month <= end.month):
        # 按月计算节气
        for solar_term in SOLAR_TERMS_MONTH[month]:
            nums = SOLAR_TERMS_C_NUMS[solar_term]
            C = nums[0] if year < 2000 else nums[1]
            # 2000 年的小寒、大寒、立春、雨水按照 20 世纪的 C 值来算
            if year == 2000 and solar_term in [
                SolarTerms.lesser_cold,
                SolarTerms.greater_cold,
                SolarTerms.the_beginning_of_spring,
                SolarTerms.rain_water,
            ]:
                C = nums[0]
            Y = year % 100
            L = int(Y / 4)
            if solar_term in [
                SolarTerms.lesser_cold,
                SolarTerms.greater_cold,
                SolarTerms.the_beginning_of_spring,
                SolarTerms.rain_water,
            ]:
                L = int((Y - 1) / 4)
            day = int(Y * D + C) - L
            # 计算偏移量
            delta = SOLAR_TERMS_DELTA.get((year, solar_term))
            if delta:
                day += delta
            _date = datetime.date(year, month, day)
            if _date < start or _date > end:
                continue
            result.append((_date, solar_term.value[1]))
        if month == 12:
            year, month = year + 1, 1
        else:
            month += 1
    return result
