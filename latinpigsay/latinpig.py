# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 19:35:55 2014

@author: steven_c
@author email: steven.e.cutting@gmail.com
@project site: https://github.com/steven-cutting/

"""

import samples
import charpool
from misc import platin

import re


platin(listofwords)


class piglatin(object):
    
    def __init__(self, string):
        self.string = string
    
    # -------------------------------------------------------------------------
    # Meta-data Creation    
    
    def _isnumber(word):
        try:
            int(word)
            return True
        except ValueError:
            return False
    
    def _classify(word):
    
        word = word.lower()
    
        if "y" in word:
            print "{}: has a y".format(word)
        elif word[0] in vowels:
            print "{}: starts with a vowel".format(word)
        elif (_isnumber(word)):
            print '{}: is a number. ------- !!'.format(word)
        else:
            print "{}: starts with cont/cont-c".format(word)
    
    def _multiplewords(string):
        return re.split(r'[;,\s]\s*', string)
    
    
    def _sentences(string):
        pass





    
def test(stuff):
    for item in stuff:
        _classify(item)

test(listofwords)

print type(int(listofwords[12]))


print '\n-----\n'

print paragraphs.count('\n\n')