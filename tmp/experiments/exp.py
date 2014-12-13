# -*- coding: utf-8 -*-
__title__ = 'latinpigsay'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/7/2014'

from data.text import samples as sam
from data import charpool as charp
from latinpigsay import generalfunctions as gfunc

import re
import string
from string import ascii_letters


class translator(object):

    def __init__(self, text):
        # Separates text into words and whitespace
        self.__listofwords = re.findall(r'(?:\S+)|(?:\s+)', text)
        self.__output = []
        self.__translated =self.buildstring()

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
            # Whitespace does not require translation
            if not word.strip():
                self.__output.append(word)
                continue
            # Punctuation does not require translation
            if not set(ascii_letters).intersection(word):
                self.__output.append(word)
                continue
            word2 = rmcon.replace(word)
            if word2 is not word:
                if word[0].isupper():
                    word2 = word2.capitalize()
                self.__parsewords(re.findall(r'(?:\S+)|(?:\s+)', word2))
            else:
                # compiled versions of most recent patterns are cached
                # So no need to precompile
                m = re.match(r'^(?P<pre>[\W]*)(?P<word>.+?)(?P<post>[\W]*)$', word)
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

"""
## The Rules Of PigLatin
**Words beginning with consonants**
    + Move the cont/conts from the start to the end.
    + Then add the suffix "ay" to the end of the word.
    + Ex.:
        - hello : ellohay
        - duck : uckday
        - switch : itchsway
        - glove : oveglay
        - fruit smoothie : uitfray oothiesmay
**Words beginning with vowels**
    + Simply add "yay" to the end.
    + Ex.:
        - it : ityay
        - egg : eggyay
        - ultimate : ultimateyay
        - I : iyay
**Words containing the letter "Y"**
    + If the word starts with the letter "Y":
        - Treat the "y" like a consonant and move
            it to the end.
        - Then add "ay"
        - Ex.:
            - yellow : ellowyay
    + elif "y" is the second letter in a two letter word:
        - The "normal rules apply.
        - Ex.:
            - my : ymay
    + elif if "y" comes at the end of a consonant cluster:
        - Treat the "y" like a vowel.
        -Ex.:
            - rhythm : ythmrhay
**4Learn how to deal with compound words.**
Compound words work better in Pig Latin when they are split up, as it makes them less comprehensible to listeners.
For example, the word "bedroom" becomes ed-bay oom-ray rather than "edroom-bay", which is more obvious.
Another example is the word "toothbrush", which becomes ooth-tay ush-bray rather than "oothbrush-tay".
"""




