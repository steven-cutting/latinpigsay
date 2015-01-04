# -*- coding: utf-8 -*-
__title__ = 'latinpigsay'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/7/2014'

if __name__ == "__main__":
    from tests import testscript as ts
    from tests import contstests
    from latinpigsay.tmp.experiments import exp
    from data.text import samples as sam

    from latinpigsay import latinpig as lp
    from latinpigsay import piggyprint as pp

    import sys

    import logging
    logging.basicConfig(filename='tests.log')

    testtorun = sys.argv[1]

    if testtorun == 'contspara':
        contstests.contsparatest()
