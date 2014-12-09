"""
__author__ = 'steven_c'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/7/2014'
"""

import requests as re
import piglatinp as pl


# Used in:
# piggyprint.py
def findlongeststing(listofstrings, minimum=0):
    length = max([len(string) for string in listofstrings])
    if length <= minimum:
        return minimum
    else:
        return length


# Used in:
# piggyprint.py
def stringframer(line, spacers='', start='<', end='>', afterstart=' ',
               beforeend=' '):
    return "{a}{b}{c}{d}{e}{f}".format(a=start,
                                   b=afterstart,
                                   c=line,
                                   d=spacers,
                                   e=beforeend,
                                   f=end,
                                   )


class onlinetext(object):
    def __init__(self, url, name=''):
        self.__url = url
        self.name = self.__pickname(url, name)
        self.__text = re.get(self.__url).text
        self.translated = ''

    def __str__(self):
        return self.__text

    def __pickname(self, url, name):
        if name is '':
            return url
        else:
            return name

    def savetext(self, filename, extension='txt'):
        fullfilename = self.__newfilename(filename, extension)
        self.__writetexttofile(self.__text, fullfilename)

    def savetranslation(self, filename, extension='txt'):
        fullfilename = self.__newfilename(filename, extension)
        self.__writetexttofile(self.__translated, fullfilename)

    @property
    def text(self):
        return self.__text

    @property
    def translation(self):
        return self.__translated

    def __writetexttofile(self, itemtowrite, filename):
            with open(filename, "w") as f:
                f.write(itemtowrite)

    def __newfilename(self, filename, extension='.txt', maxrecursivedepth=10):
        """maxrecursivedepth is used to limit the number of tries."""
        count = 0

        def namegenloop(name, counter, maxrecursivedepth):
            try:
                with open(name, 'r') as f:
                    if count is 0:
                        return name
                    else:
                        return '{n}({c})'.format(n=name, c=str(count))
            except (IOError):
                counter += 1
                if counter >= maxrecursivedepth:
                    namegenloop(name, counter, maxrecursivedepth)

        generatedname = namegenloop(filename, count)
        return generatedname + extension
