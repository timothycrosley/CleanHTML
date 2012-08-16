#!/usr/bin/env python

from distutils.core import setup

setup(name='CleanHTML',
      version='0.1',
      description='A Very Forgiving HTML/XML Cleaner.',
      author='Timothy Crosley',
      author_email='timothy.crosley@gmail.com',
      url='http://www.simpleinnovation.org/',
      download_url='https://github.com/timothycrosley/CleanHTML/blob/master/dist/CleanHTML-0.1.tar.gz?raw=true',
      license = "GNU GPLv2",
      scripts=['scripts/cleanHTML',],
      requires = ['webelements',],)
