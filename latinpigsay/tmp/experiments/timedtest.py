# -*- coding: utf-8 -*-
__title__ = 'latinpigsay'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/3/2014'


def func1(listofstrings):
    return max([len(string) for string in listofstrings])


def func2(listofstrings):
    return max(len(string) for string in listofstrings)

def func3(listofstrings):
    return len(max(mylist, key=len))






# handle a massive file using generator
def filereader_gen(file):
    with open(file) as f:
        for line in f:
            yield line


def fileprocessor(file, function):
    filegen = filereader_gen()
    filegen2 = (process(x) for x in g)




##
# Iterate over the lines of a string

foo = """
this is
a multi-line string.
"""

def f1(foo=foo): return iter(foo.splitlines())

def f2(foo=foo):
    retval = ''
    for char in foo:
        retval += char if not char == '\n' else ''
        if char == '\n':
            yield retval
            retval = ''
    if retval:
        yield retval

def f3(foo=foo):
    prevnl = -1
    while True:
      nextnl = foo.find('\n', prevnl + 1)
      if nextnl < 0: break
      yield foo[prevnl + 1:nextnl]
      prevnl = nextnl

if __name__ == '__main__':
  for f in f1, f2, f3:
    print list(f())
