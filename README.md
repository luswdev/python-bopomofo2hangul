# python-bopomofo2hangul

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
