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


## 关键定义

由于我国节假日实行“调休补班”机制，“节假日”的范畴容易产生歧义。为统一认知，此处明确本项目对核心概念的定义，避免使用混淆。

**我国节假日相关日期的常见场景**

结合调休规则，日期属性可分为以下6类：

1. [法定年节假日](https://www.gov.cn/zhengce/content/202411/content_6986380.htm)（即法定休假日，元旦1天、春节4天、清明节1天、劳动节2天、端午节1天、中秋节1天、国庆节3天）
2. 调休放假日（因节假日调休而额外放假的日期）
3. 节假日连接的周末（与假期连休的周末日期）
4. 调休工作日（因节假日调休而需要上班的休息日）
5. 普通工作日（非调休的正常上班日）
6. 普通周末（非调休、非连休的周六/周日）

**项目核心概念定义**

本项目通过两个核心概念区分日期属性，覆盖上述所有场景：

- **holiday**：休息日，包含「普通周末」「法定年节假日」「调休放假日」「节假日连接的周末」。
- **workday**：工作日，包含「普通工作日」「调休工作日」。

**核心接口返回值说明**

接口 `get_holiday_detail` 返回值 `on_holiday` 和 `holiday_name` 的不同组合，表示不同日期属性，规则如下：

| 组合场景            | on_holiday = True（休息日）                                  | on_holiday = False（工作日）     |
| :------------------ | :----------------------------------------------------------- | :------------------------------- |
| holiday_name = None | 普通周末（无特定节日属性的休息日）                           | 普通工作日（无调休关联的上班日） |
| holiday_name ≠ None | 法定节假日/调休放假日/假期连休周末（即“有节日属性的休息日”） | 因该节日调休补班的工作日         |




## 贡献代码

1. Fork + Clone 项目到本地，安装 [uv](https://docs.astral.sh/uv/) 后执行 `make install`
2. 修改[节假日定义][scripts/data.py]
3. 执行 `make fmt`，它会调用[脚本][scripts/__init__.py]自动生成[常量文件][constants.py]并格式化代码
4. 执行 `make test` 确认检查和测试都通过
5. 提交PR

[constants.py]: https://github.com/liriansu-opus/chinese-calendar/blob/master/chinese_calendar/constants.py
[scripts/data.py]: https://github.com/liriansu-opus/chinese-calendar/blob/master/chinese_calendar/scripts/data.py
[scripts/__init__.py]: https://github.com/liriansu-opus/chinese-calendar/blob/master/chinese_calendar/scripts/__init__.py
