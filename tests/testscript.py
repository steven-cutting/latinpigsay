# -*- coding: utf-8 -*-
__title__ = 'latinpigsay'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/7/2014'

from data.text import samples as sam
from latinpigsay import generalfunctions as gfunc
from tmp.experiments import expfunctions as expfunc

from latinpigsay import latinpig as lp
from latinpigsay import piggyprint as pp
from tmp.experiments import exp

from data.contractionstuple import CONTS

# import piglatin as pl

from itertools import izip

import arrow

'''
bookgot = requests.get("http://www.gutenberg.org/files/2600/2600.txt")
thebook = bookgot.text
pigbook = pl.translate(thebook)

print pigbook[170:200]
'''


files = {1 : {'file1' : 'data/text/phrases_english.txt',
              'file2' : 'data/text/phrases_piglatin.txt',
             },
         2 : {'file1' : 'data/text/contractions.txt',
              'file2' : 'data/text/contractions-un.txt'
             },
        }

def testconts():
    for word in CONTS:
        print gfunc.iscont(word[0])


def warandpeace():
    t1 = arrow.now()

    text = gfunc.onlinetext('http://www.gutenberg.org/files/2600/2600.txt',
                            'WarAndPeace').text

    #pp.piggyprint(lp.translator(text).returnstr).printall
    print lp.translator(text).returnstr
    t2 = arrow.now()
    print '\n\n'
    pp.piggyprint(str(t2 - t1)).printall

def compare(files=files):
    print type(files[1])
    for i in files:
        print i
        print '-'*50
        comparer(**i)

def compare2(files=files[1]):
    comparer(**files)

def comparer(file1, file2):
    gen = expfunc.filereader_gen

    for e, p in izip(gen(file1), gen(file2)):
        print e
        print lp.translate(e)
        print p
        print pl.translate(e)
        print exp.translate(e)
        #print exp.regexpreplacer(e)
        print '--'

def test(translator=0):
    if translator is 0:
        translated = lp.translator(sam.acidtest).returnstr
    elif translator is 1:
        translated = exp.translator(sam.acidtest).returnstr
    elif translator is 2:
        translated = translate(sam.acidtest)
    print '\n--\n'
    pp.piggyprint(translated).printall
    print '\n--\n'

def test1(translator=0):
    if translator is 0:
        translated = lp.translator(sam.paragraphs).returnstr
    elif translator is 1:
        translated = exp.translator(sam.paragraphs).returnstr
    elif translator is 2:
        translated = translate(sam.paragraphs)
    print '\n--\n'
    pp.piggyprint(translated).printall
    print '\n--\n'

def test2():
    trans1 = exp.translator(sam.quotes).returnstr
    trans2 = exp.translator(sam.simplepgs).returnstr
    print '\n--\n'
    pp.piggyprint(trans1).printall
    print '\n'
    pp.piggyprint(trans2).printall
    print '\n--\n'

def test3():
    trans1 = lp.translator(sam.paragraphs).returnstr
    trans2= lp.translator(sam.paragraphs_og).returnstr
    print '\n--\n'
    pp.piggyprint(trans1).printall
    print '\n'
    pp.piggyprint(trans2).printall
    print '\n--\n'

def test4():
    translated = lp.translator(sam.txt).returnstr
    print '\n--\n'
    pp.piggyprint(translated).printall
    print '\n--\n'

def multiprint(n=5):
    translated = lp.translator(sam.simplepgs).returnstr
    test1 = pp.piggyprint(translated)
    print '\n--\n'
    for i in xrange(n):
        print '--'
        print i
        print '--'
        test1.printall
    print '\n--\n'

