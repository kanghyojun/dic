#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

from dic import __version__


requirements = ['pytest==2.3.5', 'requests==1.2.3', 'lxml==3.2.3']

setup(name='dic.py',
      version='%s.%s.%s' % __version__,
      author='Kang Hyojun',
      author_email='hyojun@admire.kr',
      install_requires=requirements,
      packages=find_packages(),
      entry_points={
          'console_scripts': ['dic = dic.script:main']
      })
