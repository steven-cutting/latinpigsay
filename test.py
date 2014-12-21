# -*- coding: utf-8 -*-
__title__ = 'latinpigsay'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/7/2014'

if __name__ == "__main__":
    from tests import testscript as ts
    from tmp.experiments import exp
    from data.text import samples as sam

    from latinpigsay import latinpig as lp
    from latinpigsay import piggyprint as pp


    import logging
    logging.basicConfig(filename='tests.log')

    #ts.compare2()


    # ts.warandpeace()


    print '-'*30
    print '\n'

    print exp.translator(sam.paragraphs)

    '''print '\n\n'
    print '-'*30
    print '\n'
    exp.translate('asgg .,-2% \nsrg. 5')
    print '\n\n'
    '''
    print '-'*30
    print '\n'
    print exp.translator('Derp derp.')
    print '\n\n'
    #print pl.translate('Derp derp.')
    #print lp.translate('Derp derp.')


    ts.test(1)
    ts.test1(1)
    ts.test2()
    #ts.test3()
    #ts.test4()
    #ts.multiprint(2)

