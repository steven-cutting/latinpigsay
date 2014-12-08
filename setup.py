from setuptools import setup, find_packages
from codecs import open
from os import path



setup(
      name='latinpigsay'
      version='1.1a.0.dev1'
      description='Translates text into Pig Latin and and optionally provides a pretty print similar to cowsay.'

      url=''
      author='steven_c'
      author_email='steven.c.projects@gmail.com'

      packages=find_packages(exclude=['tests*']),

      classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Linux Users',
        'Topic :: Fun',

        'License :: MIT License',

        'Programing Language :: Python :: 2',
        'Programing Language :: Python :: 2.7',
        ],

        keywords='cowsay piglatin fun recreational'

        install_requires = []
)
