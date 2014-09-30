dic
===

CLI for endic, krdic

설치
-----

현재는 python3.4를 지원합니다.

[github repository][repo] 를 clone하신후 설치하시면됩니다

    $ git clone git@github.com:admire93/dic.git dic.py
    $ cd dic.py
    $ python setup.py install

사용법
--------

사용법은 아주간단한데, `dic` 명령어를 사용하시면됩니다.

    $ dic en 단어
    word, vocabulary

기본적으로 `dic` 디렉토리 내부에 있는 `conf.ini`를 읽어서
번역기 설정을 하게되어있습니다.


dic 설정하기
---------------

`dic` 명령어는 기본적으로 `dic`이 설치된 디렉토리에 있는 `conf.ini`를 읽도록
설정되어 있습니다. 만약 다른 설정 파일을 바꾸고싶다면, 환경변수를 설정하거나
`dic` 명령어의 `--config` 혹은 `-c` 옵션을 이용하여 바꿀수있습니다. 환경변수로
설정파일을 바꾸기위해서 다음 환경변수를 추가하면됩니다.

    $ export DIC_CONFIGURATION_FILE=/path/to/your/conf.ini

또는 명령어의 옵션을 이용해서 바꿀 수 있습니다.

    $ dic --config /path/conf/conf.ini en 단어


dic 확장하기
---------------

`dic` 은 설정파일을 확장해서 더 많은 단어 번역 명령을 만들어 낼 수 있습니다.
만약 `jp` 라는 명령어를 만들고 싶다면, `conf.ini` 에 `jp` 명령어와 관련된
규칙을 정의하면됩니다. 첫번째로 `language.support` 에 `,`로 구분하여 명령어를
추가합니다.

    $ cat conf.ini
    [language]
    support = en, jp

    ...


`language.support` 에 명령어를 추가했다면 명령어와 동일한 이름으로 새로운
섹션을 생성해야합니다. 해당 세션에는 `name`, `url`, `path`를 설정해줘야합니다.

    $ cat conf.ini
    [language]
    support = en, jp

    [en]
    ...

    [jp]
    name = ko.to.jp
    url = http://jptranslator.com/query={}
    path = //dt[contains(@class, "mean_on")]//em


 - `name` : 내부에서 사용되는 이름을 지정합니다.
 - `url`: 단어를 번역해올 url을 지정합니다. 단어가 들어갈부분을 `{}`로 만들어야합니다.
 - `path`: 번역된 단어가있는 문서의 위치를 [xpath][xpath] 를 이용해서 지정합니다. 한개 이상의 xpath는 `||` 로 구분하여 지정합니다.



[repo]: https://github.com/admire93/dic
[xpath]: http://en.wikipedia.org/wiki/XPath
