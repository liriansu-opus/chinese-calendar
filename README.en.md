# Chinese Calendar

[![Package](https://img.shields.io/pypi/v/chinesecalendar.svg)](https://pypi.python.org/pypi/chinesecalendar)
[![Travis](https://img.shields.io/travis/liriansu-opus/chinese-calendar.svg)](https://travis-ci.org/liriansu-opus/chinese-calendar)
[![License](https://img.shields.io/github/license/liriansu-opus/chinese-calendar.svg)](https://github.com/liriansu-opus/chinese-calendar/blob/master/LICENSE)
[![README](https://img.shields.io/badge/简介-中文-brightgreen.svg)](https://github.com/liriansu-opus/chinese-calendar/blob/master/README.md)

Check if some date is workday or holiday in China.
Support 2004 ~ 2027.

## Installation

```
pip install chinesecalendar
```

## Upgrade

```
pip install -U chinesecalendar
```

Chinese government announces holiday arrangement usually during November.
This project will release new version after official announcement.

## Sample

``` python
import datetime

# Check if 2018-04-30 is holiday in China
from chinese_calendar import is_holiday, is_workday
april_last = datetime.date(2018, 4, 30)
assert is_workday(april_last) is False
assert is_holiday(april_last) is True

# or check and get the holiday name
import chinese_calendar as calendar  # 也可以这样 import
on_holiday, holiday_name = calendar.get_holiday_detail(april_last)
assert on_holiday is True
assert holiday_name == calendar.Holiday.labour_day.value

# even check if a holiday is in lieu
import chinese_calendar
assert chinese_calendar.is_in_lieu(datetime.date(2006, 2, 1)) is False
assert chinese_calendar.is_in_lieu(datetime.date(2006, 2, 2)) is True
```

## Other Languages

If you fail to use Python directly,
you can translate the [constants file][constants.py] to get the complete chinese holiday arrangement.

## Contributing

1. Fork & Clone this project
2. Modify [calendar definition file][scripts/data.py]
3. Run [script][scripts/__init__.py] to generate the [constants file][constants.py]
4. Create a PR

[constants.py]: https://github.com/liriansu-opus/chinese-calendar/blob/master/chinese_calendar/constants.py
[scripts/data.py]: https://github.com/liriansu-opus/chinese-calendar/blob/master/chinese_calendar/scripts/data.py
[scripts/__init__.py]: https://github.com/liriansu-opus/chinese-calendar/blob/master/chinese_calendar/scripts/__init__.py
