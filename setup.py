# -*- coding: utf-8
# author: zarhin
# date: 2020/7/21 16:35

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(name='function',
      version='0.0.1',
      description='Some common and useful function',
      author='zarhin',
      author_email='lizaixianvip@live.com',
      packages=find_packages(exclude=('tests', 'docs')))
