# -*- coding: utf-8 -*-
import pytest

from dictionary import Dictionary, get_dictionary

def test_not_implemented_error():
    with pytest.raises(Exception):
        translator = Dictionary()
        translator.word = 'def'

def test_generate_translator_from_option():
    options = {
        'name': 'test.ko.to.en',
        'url': 'http://test.com',
        'path': 'div#content > span'
    }
    t = get_dictionary(**options)
    t.word = 'echo'
    assert 'echo' == t.word


def test_naver_dictionary():
    options = {
        'name': 'naver.ko.to.en',
        'url': u'http://endic.naver.com/search.nhn?query={0}',
        'path': '//dt[contains(@class, \'mean_on\')]//em//span[@class=\'EQUIV\']'
    }
    t = get_dictionary(**options)
    t.word = u'안녕'
    res = t.word.split(', ')
    assert res
    assert 'hello' in res
