# -*- coding: utf-8 -*-

import pytest
from pybopomofo2hangul import bopomofo_to_hangul

def test_initial_bopomofo():
    assert bopomofo_to_hangul('奔') == '번' # ㄅ
    assert bopomofo_to_hangul('噴') == '펀' # ㄆ
    assert bopomofo_to_hangul('悶') == '먼' # ㄇ
    assert bopomofo_to_hangul('分') == '펀' # ㄈ
    assert bopomofo_to_hangul('燈') == '덩' # ㄉ
    assert bopomofo_to_hangul('疼') == '텅' # ㄊ
    assert bopomofo_to_hangul('能') == '넝' # ㄋ
    assert bopomofo_to_hangul('稜') == '렁' # ㄌ
    assert bopomofo_to_hangul('歌') == '거' # ㄍ
    assert bopomofo_to_hangul('科') == '커' # ㄎ
    assert bopomofo_to_hangul('喝') == '허' # ㄏ
    assert bopomofo_to_hangul('機') == '지' # ㄐ
    assert bopomofo_to_hangul('七') == '치' # ㄑ
    assert bopomofo_to_hangul('西') == '시' # ㄒ
    assert bopomofo_to_hangul('之') == '즈' # ㄓ
    assert bopomofo_to_hangul('吃') == '츠' # ㄔ
    assert bopomofo_to_hangul('師') == '스' # ㄕ
    assert bopomofo_to_hangul('日') == '르' # ㄖ
    assert bopomofo_to_hangul('字') == '쯔' # ㄗ
    assert bopomofo_to_hangul('次') == '츠' # ㄘ
    assert bopomofo_to_hangul('四') == '쓰' # ㄙ

def test_final_bopomofo():
    assert bopomofo_to_hangul('衣') == '이' # 一
    assert bopomofo_to_hangul('汙') == '우' # ㄨ
    assert bopomofo_to_hangul('瘀') == '위' # ㄩ
    assert bopomofo_to_hangul('啊') == '아' # ㄚ
    assert bopomofo_to_hangul('喔') == '오' # ㄛ
    assert bopomofo_to_hangul('餓') == '어' # ㄜ
    assert bopomofo_to_hangul('鐵') == '톄' # ㄝ
    assert bopomofo_to_hangul('愛') == '아이' # ㄞ
    assert bopomofo_to_hangul('被') == '베이' # ㄟ
    assert bopomofo_to_hangul('奧') == '아오' # ㄠ
    assert bopomofo_to_hangul('歐') == '어우' # ㄡ
    assert bopomofo_to_hangul('安') == '안' # ㄢ
    assert bopomofo_to_hangul('恩') == '언' # ㄣ
    assert bopomofo_to_hangul('盎') == '앙' # ㄤ
    assert bopomofo_to_hangul('騰') == '텅' # ㄥ
    assert bopomofo_to_hangul('二') == '얼' # ㄦ

def test_double_final_bopomofo():
    assert bopomofo_to_hangul('鴨') == '야' # ㄧㄚ
    assert bopomofo_to_hangul('唷') == '요' # ㄧㄛ
    assert bopomofo_to_hangul('也') == '예' # ㄧㄝ
    # assert bopomofo_to_hangul('崖') == '야이' # ㄧㄞ
    assert bopomofo_to_hangul('腰') == '야오' # ㄧㄠ
    assert bopomofo_to_hangul('又') == '유' # ㄧㄡ
    assert bopomofo_to_hangul('眼') == '옌' # ㄧㄢ
    assert bopomofo_to_hangul('音') == '인' # ㄧㄣ
    assert bopomofo_to_hangul('央') == '양' # ㄧㄤ
    assert bopomofo_to_hangul('應') == '잉' # ㄧㄥ
    assert bopomofo_to_hangul('挖') == '와' # ㄨㄚ
    assert bopomofo_to_hangul('我') == '워' # ㄨㄛ
    assert bopomofo_to_hangul('歪') == '왜' # ㄨㄞ
    assert bopomofo_to_hangul('對') == '두이' # ㄨㄟ
    assert bopomofo_to_hangul('灣') == '완' # ㄨㄢ
    assert bopomofo_to_hangul('燉') == '둔' # ㄨㄣ
    assert bopomofo_to_hangul('轟') == '훙' # ㄨㄥ
    assert bopomofo_to_hangul('月') == '웨' # ㄩㄝ
    assert bopomofo_to_hangul('淵') == '위안' # ㄩㄢ
    assert bopomofo_to_hangul('運') == '윈' # ㄩㄣ
    assert bopomofo_to_hangul('用') == '융' # ㄩㄥ

def test_alone_double_final_bopomofo():
    assert bopomofo_to_hangul('威') == '웨이' # ㄨㄟ
    assert bopomofo_to_hangul('溫') == '원' # ㄨㄣ
    assert bopomofo_to_hangul('翁') == '웡' # ㄨㄥ

def test_tone():
    assert bopomofo_to_hangul('哀') == bopomofo_to_hangul('癌') # ˉ == ˊ
    assert bopomofo_to_hangul('哀') == bopomofo_to_hangul('矮') # ˉ == ˇ
    assert bopomofo_to_hangul('哀') == bopomofo_to_hangul('愛') # ˉ == ˋ
    assert bopomofo_to_hangul('八') == bopomofo_to_hangul('吧') # ˉ == ˙
    assert bopomofo_to_hangul('癌') == bopomofo_to_hangul('矮') # ˊ == ˇ
    assert bopomofo_to_hangul('癌') == bopomofo_to_hangul('愛') # ˊ == ˋ
    assert bopomofo_to_hangul('拔') == bopomofo_to_hangul('吧') # ˊ == ˙
    assert bopomofo_to_hangul('矮') == bopomofo_to_hangul('愛') # ˇ == ˋ
    assert bopomofo_to_hangul('把') == bopomofo_to_hangul('吧') # ˇ == ˙
    assert bopomofo_to_hangul('罷') == bopomofo_to_hangul('吧') # ˋ == ˙

def test_symbol():
    assert bopomofo_to_hangul('，。：；！？「」『』') == bopomofo_to_hangul('，。：；！？「」『』')

def test_empty_string():
    assert bopomofo_to_hangul('') == ''

def test_sample_string():
    assert bopomofo_to_hangul('你好，世界！') == '니하오，스제！'
