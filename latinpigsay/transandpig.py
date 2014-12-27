# -*- coding: utf-8 -*-
__title__ = 'latinpigsay'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/27/2014'

import sys
import piglatin as pl

from latinpigsay import latinpig as lp
from latinpigsay import piggyprint as pp
from tmp.experiments import exp


def latinpigsay(text, exp='no'):
    if exp in ('no', 'n'):
        translated = lp.translator(text).returnstr
    elif exp in ('yes', 'y'):
        translated = exp.translator(text).returnstr
    else:
        sys.exit
    pp.piggyprint(translated).printall



