__author__="Ross Karchner, after Aiden Scandella"
__date__ ="$Jan 11, 2010 5:06:00 PM$"

from setuptools import setup,find_packages

setup (
  name = 'socratic',
  version = '0.2',
  packages = find_packages(),

  install_requires=['feedparser','requests','poster'],

  author = 'Ross Karchner, after Aiden Scandella',
  author_email = 'ross@karchner.com',
  license = '',
  long_description= 'A native Python implementation of Socrata\'s REST API, using JSON'
)
