# python-bopomofo2hangul

[![CI Status](https://github.com/luswdev/python-bopomofo2hangul/actions/workflows/pytest.yml/badge.svg)](https://github.com/luswdev/python-bopomofo2hangul/actions/workflows/pytest.yml)
[![CI Status](https://github.com/luswdev/python-bopomofo2hangul/actions/workflows/publish.yml/badge.svg)](https://github.com/luswdev/python-bopomofo2hangul/actions/workflows/publish.yml)
[![PyPI version](https://img.shields.io/pypi/v/pybopomofo2hangul.svg)](https://pypi.org/project/pybopomofo2hangul/)
[![Python Version](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-brightgreen.svg)](https://pypi.org/project/pybopomofo2hangul/)

Translate Ｍandarin to Hangul (한글) from bopomofo (ㄅㄆㄇㄈ).

Refer to **중국어의 한글 표기** from National Institute of the Korean Language.

## Installation

```bash
pip install pybopomofo2hangul
```

## Usage

```py
from pybopomofo2hangul import bopomofo_to_hangul

fromStr = "你好，世界"
outStr = bopomofo_to_hangul(fromStr)

print(outStr)   # will output like: "니하오，스제！"
```

## Dependencies 

- [python-pinyin](https://github.com/mozillazg/python-pinyin)
