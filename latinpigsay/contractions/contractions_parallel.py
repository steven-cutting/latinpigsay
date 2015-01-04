# -*- coding: utf-8 -*-
__title__ = 'latinpigsay'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/27/2014'


from latinpigsay.tmp.experiments import exp
from latinpigsay import generalfunctions as gfunc
from latinpigsay.tmp.experiments import expfunctions as expfunc

from latinpigsay.contractions import find_contractions as findconts
from data.contractionstuple import JUST_CONTS

from itertools import islice, permutations, count, izip, imap, product, chain
import itertools
import re

import json
from xml.dom import minidom

import os
from os import path
import operator

from multiprocessing import Pool

def build_batches(listof, numofbatches):
    numberof = len(listof)
    perbatch = numberof / numofbatches
    offset = numberof - perbatch*numofbatches
    start = 0
    end = perbatch + 1
    batches = []
    for core in xrange(numofbatches):
        batches.append(listof[start:end])
        start = end
        end += perbatch
    return batches

def contspara(path, cores=1):
    filelist = [''.join([path, file]) for file in os.listdir(path) if file.endswith('.txt')]
    numberoffiles = len(filelist)
    filespercore = numberoffiles / cores
    filebatches = build_batches(filelist, cores)
    print filebatches
    def countfromgenlist_parallel(filelist):
        filegen_factory = lambda filelist: itertools.imap(gfunc.fileline, filelist)
        #filebatch_gen = lambda filebatches: map(filegen_factory, filebatches)


        return findconts.countfromgenlist(filegen_factory(filelist), JUST_CONTS)


    def contsinparallel(filebatches):
        pool = Pool(processes=cores)
        results = pool.map(countfromgenlist_parallel, filebatches)
        product = results
        return product

    with gfunc.Timer() as t:
        listofresults = contsinparallel(filebatches)
    print t.interval

    print listofresults

