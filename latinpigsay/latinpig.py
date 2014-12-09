__title__ = 'latinpigsay'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/7/2014'

from data.text import samples as sam
from data import charpool as charp
import generalfunctions as gfunc

import re
import string
from string import ascii_letters


class regexpreplacer(object):
    def __init__(self, patterns):
        self.patterns = [(re.compile(regex), repl) for (regex, repl) in
                         patterns]
    def replace(self, text):
        s = text
        for (pattern, repl) in self.patterns:
            (s, count) = re.subn(pattern, repl, s)
        return s



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




# ------------------------------------------------------------------------------
# Depreciated


def makestringiter(string):
    re.finditer(r'(?:\S+)|(?:\s+)', string)



class translation(object):

    def __init__(self, string):
        self.listofstrings = string.splitlines()


cont = 'c'
vowel = 'v'
y = 'y'




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





"""
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
"""
