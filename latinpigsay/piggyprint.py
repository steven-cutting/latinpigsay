__author__ = 'steven_c'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/7/2014'


from data.pigs import piggies

import piglatinp as pl
import generalfunctions as gfunc


class piggyprint(object):
    """Prints an ASCII pig with a speech bubble above it.
    The speech bubble contains the string provided when creating an instance of
    this class.
    Using the initiation argument 'character', a different ASCII character can
    be provided.
    """
    def __init__(self, string=' ', character=piggies.pig):
        # ASCII character printed bellow the speech bubble.
        self.character = character # Not private because it's OK to change.
        # Metadata about the ASCII character.
        self.__minlinelen = gfunc.findlongeststing(self.character.splitlines())

        # List made up of lines from the supplied string.
        self.__listofstrings = string.splitlines()
        # Metadata about the above list used to make the Speech Bubble.
        self.__longeststring = gfunc.findlongeststing(self.__listofstrings,
                                                      self.__minlinelen)
        self.__lenoflist = len(self.__listofstrings)
        # Parts of the Speech Bubble
        self.__bubbletop = ' {}'.format('_' * (self.__longeststring + 2))
        self.__bubblebody = self.__bubblebodyiter
        self.__bubblebottom = ' {}'.format('-' * (self.__longeststring + 2))

    def __str__(self):
        pass

    def __bubblebodyiter(self):
        for n, string_n in enumerate(self.__listofstrings):
            length = 0
            gap = 0
            if string_n is '':
                gap = self.__longeststring
                spacers = " " * gap
            else:
                length = len(string_n)
                gap = self.__longeststring - length
                spacers = " " * gap

            if self.__lenoflist is 1:
                yield gfunc.stringframer(string_n)
            elif n is 0:
                yield gfunc.stringframer(string_n, spacers, '/', '\\')
            elif n is self.__lenoflist - 1:
                yield gfunc.stringframer(string_n, spacers, '\\', '/')
            else:
                yield gfunc.stringframer(string_n, spacers, '|', '|')

    @property
    def __printbubble(self):
        print self.__bubbletop
        body = self.__bubblebody()
        for line in body:
            print line
        print self.__bubblebottom

    @property
    def printall(self):
        self.__printbubble
        print self.character

