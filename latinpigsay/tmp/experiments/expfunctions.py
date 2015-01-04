# -*- coding: utf-8 -*-
__title__ = 'latinpigsay'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/7/2014'

# handle a massive file using generator
def filereader_gen(file):
    with open(file) as f:
        for line in f:
            yield line
