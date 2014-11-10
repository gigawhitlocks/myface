#!/usr/bin/env python

from setuptools import setup

setup(name='iansface', 
      version='1.0',
      description='A module for printing Ian\'s face.',
      author='gigawhitlocks',
      author_email='giggles@alum.hackerschool.com',
      url='http://github.com/gigawhitlocks/myface',
      entry_points={'console_scripts': ['iansface=iansface:main']},
      download_url='https://github.com/gigawhitlocks/myface/archive/master.zip',
      py_modules=['iansface'])
