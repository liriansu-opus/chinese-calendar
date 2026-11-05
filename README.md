# 中国节假日

[![Package](https://img.shields.io/pypi/v/chinesecalendar.svg)](https://pypi.python.org/pypi/chinesecalendar)
[![License](https://img.shields.io/github/license/liriansu-opus/chinese-calendar.svg)](https://github.com/liriansu-opus/chinese-calendar/blob/master/LICENSE)
[![README](https://img.shields.io/badge/README-English-brightgreen.svg)](https://github.com/liriansu-opus/chinese-calendar/blob/master/README.en.md)

判断某年某月某一天是不是工作日/节假日。
支持 2004年 至 2027年，包括 2020年 的春节延长。

## 安装

```
pip install chinesecalendar
```

## 升级

```
pip install -U chinesecalendar
```

由于次年的节假日安排，取决于国务院发布的日程。
所以本项目一般会在国务院更新以后，发布新的版本。
按照以往的经验，一般是每年的 11月 前后发布新版本。

## 样例

``` python
import datetime

# 判断 2018年4月30号 是不是节假日
from chinese_calendar import is_holiday, is_workday
april_last = datetime.date(2018, 4, 30)
assert is_workday(april_last) is False
assert is_holiday(april_last) is True

# 或者在判断的同时，获取节日名
import chinese_calendar as calendar  # 也可以这样 import
on_holiday, holiday_name = calendar.get_holiday_detail(april_last)
assert on_holiday is True
assert holiday_name == calendar.Holiday.labour_day.value

# 还能判断法定节假日是不是调休
import chinese_calendar
assert chinese_calendar.is_in_lieu(datetime.date(2006, 2, 1)) is False
assert chinese_calendar.is_in_lieu(datetime.date(2006, 2, 2)) is True
```

## 其它语言

假如你没法使用Python，
你也可以转译现成的[常量文件][constants.py]来获取最全的节假日安排表。

## 贡献代码

1. Fork + Clone 项目到本地，安装 [uv](https://docs.astral.sh/uv/) 后执行 `make install`
2. 修改[节假日定义][scripts/data.py]
3. 执行 `make fmt`，它会调用[脚本][scripts/__init__.py]自动生成[常量文件][constants.py]并格式化代码
4. 执行 `make test` 确认检查和测试都通过
5. 提交PR

[constants.py]: https://github.com/liriansu-opus/chinese-calendar/blob/master/chinese_calendar/constants.py
[scripts/data.py]: https://github.com/liriansu-opus/chinese-calendar/blob/master/chinese_calendar/scripts/data.py
[scripts/__init__.py]: https://github.com/liriansu-opus/chinese-calendar/blob/master/chinese_calendar/scripts/__init__.py
