# -*- coding: utf-8 -*-
__title__ = 'latinpigsay'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/27/2014'


from latinpigsay.tmp.experiments import exp
from latinpigsay import generalfunctions as gfunc
from latinpigsay.tmp.experiments import expfunctions as expfunc

from data.contractionstuple import JUST_CONTS

from itertools import islice, permutations, count, izip, imap, product, chain
import itertools
import re

import json
from xml.dom import minidom

import os
from os import path
import operator


fff = lambda path: itertools.imap(fileline,
                                  (''.join([path, file])
                                   for file in os.listdir(path)
                                   if file.endswith('.txt')))
ggg = lambda path: itertools.imap(fileword_gen,
                                  (''.join([path, file])
                                   for file in os.listdir(path)
                                   if file.endswith('.txt')))


def countfreq(word, listtocount):
    """Checks if the word is in the list (or other iterable)."""
    assert type(listtocount) in (list, tuple)
    if type(listtocount[0]) is not list:
        countlist = [[w, 0] for w in listtocount]
    elif type(listtocount[0]) is list:
        countlist = listtocount
    for thing in countlist:
        if thing[0] in word:
            thing[1] += 1
    return countlist


def countfromlist(wordgen, listtocount):
    """Checks if the text provided contains any of the words from the list
    (or other iterable).
    Returns a list of lists containing the words from the list and the number
    of times they occurred."""
    assert type(listtocount) in (list, tuple)
    if type(listtocount[0]) is not list:
        countlist = [[w, 0] for w in listtocount]
    elif type(listtocount[0]) is list:
        countlist = listtocount

    for word in wordgen:
        words = word.split()
        for w in words:
            for thing in countlist:
                if thing[0] in w:
                    thing[1] += 1
    return countlist


def countfromgenlist(genlist, listtocount):
    """Input a list of iterables and a list to of words to compare against."""
    countlist = listtocount
    try:
        gen = genlist.next()
        gengen = genlist
        countlist = countfromlist(gen, listtocount)
        countfromgenlist(gengen, countlist)

    finally:
        return countlist
