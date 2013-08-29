dic
===

CLI for endic, krdic 

설치
-----

[github repository][repo] 를 clone하신후 설치하시면됩니다

    $ git clone git@github.com:admire93/dic.git dic.py
    $ cd dic.py
    $ python setup.py install

사용법
--------

사용법은 아주간단한데, `dic` 명령어를 사용하시면됩니다.

    $ dic en 단어
    word, vocabulary

현재는 `dic.script` 내부에 있는 `options`에 있는 설정으로 
번역기 설정을 하게되어있습니다.


dic.py 확장하기
-----------------

만약 다른 언어에 번역을 하고싶다면, `dic.script`에 있는 `dic.script.options`를 
확장하면 됩니다.  일본어를 번역하기 위한 확장을 만들고싶다면

```
options['lang']['jp'] = 'some.jp.to.ko'
```

처럼 언어 옵션을 먼저 설정해줍니다. 여기서 `jp`는 `dic.py`의 첫번째 인자이며,
값은 `dictionary.Dictionary` 의 `name`입니다. 언어 옵션을 설정해주었다면 
실제 단어를 찾는 부분을 만들어야합니다.

```
options['translators'].append({
    'name': 'some.jp.to.ko',
    'url': u'http://some_translator.com/jp?query={0}',
    'path': 'xpath goes here'
})
```

번역기 부분에는 `name`, `url`, `path` 세개의 키값이 반드시 들어가야하며,

 - `name`은 언어 옵션에있는 `options['lang']['jp']`의 값과 동일해야합니다.
 - `url`은 단어가 번역되어 나오는 페이지입니다. 내부적으로 `string.format`을
   호출해서 사용하기때문에 python string format에 맞춰서 작성하면됩니다.
 - `path`는 `url` 페이지에서 번역된 단어를 찾기위한 [xpath][xpath] 입니다.
   `path`는 `basestring`이나 `list`가 될 수 있습니다.


[repo]: https://github.com/admire93/dic
[xpath]: http://en.wikipedia.org/wiki/XPath
