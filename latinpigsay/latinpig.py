# -*- coding: utf-8 -*-
__title__ = 'latinpigsay'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/3/2014'


from data import charpool as charp
import generalfunctions as gfunc

import re
import string
from string import ascii_letters

import logging
_LOG = logging.getLogger(__name__)

class translator(object):

    def __init__(self, text):
        # Separates text into words and whitespace
        self.__listofwords = re.findall(r'(?:\S+)|(?:\s+)', text)
        self.__output = []
        self.__translated = self.buildstring()

    def buildstring(self):
        self.__parsewords(self.__listofwords)
        return ''.join(self.__output)

    def __str__(self):
        return self.__translated

    @property
    def returnstr(self):
        return self.__translated

    __vowels = 'aeiouAEIOU'
    __rmcon = gfunc.regexpreplacer(charp.contractions)

    def __parsewords(self, words, vowels=__vowels, rmcon=__rmcon):
        for word in words:
            word2 = rmcon.replace(word)
            if word2 is not word:
                self.__parsewords(word2.split())
            else:
                # Whitespace does not require translation
                if not word.strip():
                    self.__output.append(word)
                    continue
                # Punctuation does not require translation
                if not set(ascii_letters).intersection(word):
                    self.__output.append(word)
                    continue
                m = re.match(r'^(?P<pre>[\W]*)(?P<word>.+?)(?P<post>[\W]*)$',
                             word
                             )
                d = m.groupdict()

                i = 0
                word = d['word']
                length = len(word)
                while length > i:
                    if word[i] in vowels:
                        break
                    if i > 0 and word[i] in 'yY':
                        break
                    i += 1

                d['fore'] = word[i:]
                d['aft'] = word[:i]

                if word[0] in vowels:
                    new_word = '%(pre)s%(fore)s%(aft)sway%(post)s' % d
                else:
                    new_word = '%(pre)s%(fore)s%(aft)say%(post)s' % d
                new_word = new_word.lower()

                #Check if fist letter is uppercase
                if word[0].isupper():
                    new_word = new_word.capitalize()

                self.__output.append(new_word)
