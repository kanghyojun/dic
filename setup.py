#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import ast


requirements = ['pytest>=2.3.5', 'requests==1.2.3', 'lxml==3.2.3']

def get_version(filename):
    with open(filename) as f:
        tree = ast.parse(f.read(), filename)
    for node in tree.body:
        if isinstance(node, ast.Assign) and node.targets[0].id == '__version__':
            version = ast.literal_eval(node.value)
            if isinstance(version, tuple):
                version = '.'.join([str(x) for x in version])
            return version
    raise Exception('__version__ not found in {}'.format(filename))


setup(name='dic.py',
      version=get_version('dic.py'),
      author='Kang Hyojun',
      author_email='hyojun@admire.kr',
      install_requires=requirements,
      packages=find_packages(),
      entry_points={
          'console_scripts': ['dic = dic.script:main']
      })
