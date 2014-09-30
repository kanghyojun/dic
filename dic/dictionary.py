# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.parse import quote

import lxml.html

__all__ = 'Dictionary', 'get_dictionary'

class Dictionary(object):

    _origin = ''
    _translate = ''

    def __init__(self, name, url):
        self.url = url
        self.name = name

    def get_meaning_from_url(self):
        raise NotImplementedError('`get_meaning_from_url` MUST implemented.')

    def translate(self, word):
        self._origin = word
        self._translate = self.get_meaning_from_url()
        return self.get_meaning_from_url()


def get_dictionary(**options):
    def f(self):
        url = self.url.format(quote(self._origin))
        with urlopen(url) as f:
            r = f.read()
        result = ''
        if not r:
            raise Exception("document didn't respond, url: {}".format(url))
        html = lxml.html.fromstring(r)
        finds = []
        paths = options['path'].split('||')
        if not paths:
            raise Exception(
                "Path didn't set properly : {}".format(options['path']))
        for p in paths:
            finds = html.xpath(p.strip())
            if len(finds):
                break
        results = [f.text_content().strip() for f in finds]
        result = ', '.join(results)
        return result

    MetaTranslator = type('Dictionary', (), dict(Dictionary.__dict__))
    setattr(MetaTranslator, 'get_meaning_from_url', f)
    return MetaTranslator(options['name'], options['url'])
