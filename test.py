from tests import testscript as ts
from tmp.experiments import exp
from data.text import samples as sam

from latinpigsay import latinpig as lp
from latinpigsay import piggyprint as pp


# ts.compare2()


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

ts.test()
ts.test1()
ts.test2()
#ts.test3()
#ts.test4()
#ts.multiprint(2)

