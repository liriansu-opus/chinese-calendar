# -*- coding: utf-8 -*-
from setuptools import setup

import chinese_calendar

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="chinesecalendar",
    version=chinese_calendar.__version__,
    description="check if some day is holiday in China",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Lirian Su",
    author_email="liriansu@gmail.com",
    url="https://github.com/liriansu-opus/chinese-calendar",
    license="MIT License",
    license_files=[],
    packages=["chinese_calendar"],
    python_requires=">=3.10",
    install_requires=[],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: 3.15",
    ],
)
