# -*- coding: utf-8 -*-
__title__ = 'latinpigsay'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/27/2014'

from latinpigsay.contractions import contractions_parallel as contspara
from latinpigsay.contractions import contractions_parallel as findconts

def contsparatest():
    contspara.contspara('data/text/testbatch/', 4)
