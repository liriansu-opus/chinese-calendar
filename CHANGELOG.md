## Latest Version 1.12.0
> on 2026-11-05

* **FEAT**: 支持 2027年 的节假日
  - 依据国务院公告，见 `https://www.gov.cn/zhengce/zhengceku/202611/content_7085102.htm`

## Version 1.11.0
> on 2025-11-04

* **FEAT**: 支持 2026年 的节假日
  - 依据国务院公告，见 `https://www.gov.cn/zhengce/content/202511/content_7047090.htm`

## Version 1.10.0
> on 2024-11-13

* **FEAT**: 支持 2025年 的节假日

## Version 1.9.2
> on 2024-09-16

* **FIX**: 修正 2025年 元旦调休标记不正确的问题，thanks @Andrea-Chenjia-Pan

## Version 1.9.1
> on 2024-02-19

* **FIX**: 修正 2024年 中秋调休标记不正确的问题，thanks @xiaomingtt

## Version 1.9.0
> on 2023-10-25

* **FEAT**: 支持 2024年 的节假日
* **FEAT**: 支持 Python3.12, 移除 Python3.7 的支持
  - 注：对低版本，本库依然可以使用 wheel 包进行安装，但不保证能正常工作

## Version 1.8.1
> on 2023-07-03

* **FEAT**: 支持 Python3.11
* **FEAT**: `get_workdays` 函数新增 `include_weekends` 筛选，该筛选关闭后会过滤掉调休的周末，thanks @Dragon-GCS #104
* **CHORE**: 更新项目开发依赖

## Version 1.8.0
> on 2022-12-09

* **FEAT**: 支持 2023年 的节假日

## Version 1.7.2
> on 2022-04-11

* **FIX**: 修复二十四节气获取会出错的问题, thanks @yqkcn

## Version 1.7.1
> on 2022-03-24

* **FIX**: 修复对 Python 2.7 的支持
  - 注：虽然本库仍然支持 Python 2.7, 但建议您升级版本至 Python 3.6+, 下一个 major 版本将不在支持 Python 2.7

## Version 1.7.0
> on 2022-03-22

* **FEAT**: 支持二十四节气的获取, thanks @yqkcn

## Version 1.6.0
> on 2021-10-26

* **FEAT**: 支持 2022年 的节假日

## Version 1.5.1
> on 2021-07-14

* **FIX**: 修复 2019年 节假日风格判定问题

## Version 1.5.0
> on 2020-11-26

* **FEAT**: 支持 2021年 的节假日

## Version 1.4.0
> on 2020-01-27

* **FEAT**: 补充 2020年 春节延长的节假日

## Version 1.3.1
> on 2019-12-12

* **FIX**: 修复 2020年9月27日 调休有误的问题

## Version 1.3.0
> on 2019-11-22

* **FEAT**: 支持 2020年 的节假日


## Version 1.2.0
> on 2018-12-18

* **FEAT**: 支持 2019年 的节假日


## Version 1.1.0
> on 2018-9-7

* **FEAT**: 支持判断调休
