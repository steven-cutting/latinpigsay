from data.text import samples as sam
from latinpigsay import generalfunctions as gfunc

from latinpigsay import latinpig as lp
from latinpigsay import piggyprint as pp
from tmp.experiments import exp

import requests as re
from itertools import izip

import arrow

'''
bookgot = re.get("http://www.gutenberg.org/files/2600/2600.txt")
thebook = bookgot.text
pigbook = pl.translate(thebook)

print pigbook[170:200]
'''


files = ({'file1' : 'data/text/phrases_english.txt',
          'file2' : 'data/text/phrases_piglatin.txt',
         },
         {'file1' : 'data/text/contractions.txt',
          'file2' : 'data/text/contractions-un.txt'
         },
        )

def warandpeace():
    t1 = arrow.now()

    text = gfunc.onlinetext('http://www.gutenberg.org/files/2600/2600.txt',
                            'WarAndPeace').text

    pp.piggyprint(lp.translator(text).returnstr).printall
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
    gen = exp.filereader_gen

    for e, p in izip(gen(file1), gen(file2)):
        print e
        print lp.translate(e)
        print p
        print pl.translate(e)
        print exp.translate(e)
        #print exp.regexpreplacer(e)
        print '--'

def test():
    translated = exp.translator(sam.acidtest).returnstr
    print '\n--\n'
    pp.piggyprint(translated).printall
    print '\n--\n'

def test1():
    translated = exp.translator(sam.paragraphs).returnstr
    print '\n--\n'
    pp.piggyprint(translated).printall
    print '\n--\n'

def test2():
    trans1 = exp.translate(sam.quotes).returnstr
    trans2 = exp.translate(sam.simplepgs).returnstr
    print '\n--\n'
    pp.piggyprint(trans1).printall
    print '\n'
    pp.piggyprint(trans2).printall
    print '\n--\n'

def test3():
    trans1 = pl.translate(sam.paragraphs)
    trans2= pl.translate(sam.paragraphs_og)
    print '\n--\n'
    pp.piggyprint(trans1).printall
    print '\n'
    pp.piggyprint(trans2).printall
    print '\n--\n'

def test4():
    translated = pl.translate(sam.txt)
    print '\n--\n'
    pp.piggyprint(translated).printall
    print '\n--\n'

def multiprint(n=5):
    translated = pl.translate(sam.simplepgs)
    test1 = pp.piggyprint(translated)
    print '\n--\n'
    for i in xrange(n):
        print '--'
        print i
        print '--'
        test1.printall
    print '\n--\n'

