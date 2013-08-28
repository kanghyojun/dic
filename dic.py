#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
from dictionary import get_dictionary

__version__ = (0, 0, 1)

options = {
    'lang': {'en': 'naver.ko.to.en'},
    'translators': [
        {
            'name': 'naver.ko.to.en',
            'url': u'http://endic.naver.com/search.nhn?query={0}',
            'path': [
                '//dt[contains(@class, \'mean_on\')]//em//span[@class=\'EQUIV\']',
                '//dd//span[contains(@class, \'fnt_k05\')]//span[@class=\'EQUIV\']'
            ]
        }
    ]
}

def setup_translator(translators):
    translator_env = {}
    for t in translators:
        inst = get_dictionary(**t)
        translator_env[inst.name] = inst

    return translator_env

def main(argv):
    if len(argv) < 3:
        print 'wrong number arguments'
        print '$ python dic.py [lang] [word]'
        return

    translators = setup_translator(options['translators'])

    if argv[1] in options['lang'] and options['lang'][argv[1]] in translators:
        trans = translators[options['lang'][argv[1]]]
        trans.word = argv[2].decode('utf-8')
        print trans.word

if __name__ == '__main__':
    main(argv)
