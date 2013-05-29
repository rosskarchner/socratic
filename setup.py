__author__="Ross Karchner, after Aiden Scandella"
__date__ ="$Jan 11, 2010 5:06:00 PM$"

from distutils.core import setup

setup (
  name = 'socratic',
  version = '0.2',
  packages = ['socratic'],

  install_requires=['requests'],
  package_dir = {'': 'src'},
  scripts=['src/socratic/scripts/socratic'],

  author = 'Ross Karchner, after Aiden Scandella',
  author_email = 'ross@karchner.com',
  license = '',
  long_description= 'A SODA (Socrata Open Data API) client library, with support for Socrata\'s extensions'
)
