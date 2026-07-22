# -*- coding: utf-8 -*-

import pytest
from pybopomofo2hangul import bopomofo_to_hangul

def test_basic_conversion():
    input_text = "你好，世界！"
    expected = "니하오，스제！"
    
    assert bopomofo_to_hangul(input_text) == expected

def test_empty_string():
    assert bopomofo_to_hangul("") == ""
