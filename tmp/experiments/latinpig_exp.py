""" Converts text to Pig Latin

>>> import piglatin
>>>
>>> piglatin.translate('this is a test string')
'is-thay is-ay a-ay est-tay ing-stray'

"""

from text import samples

from data import charpool

import re
import string
from string import ascii_letters


def makestringiter(string):
	re.finditer(r'(?:\S+)|(?:\s+)', string)


def translate(txt):
	vowels = 'aeiouAEIOU'
	# Separates text into words and whitespace
	words = re.findall(r'(?:\S+)|(?:\s+)', txt)


	output = []
	for word in words:
		# Whitespace does not require translation
		if not word.strip():
			output.append(word)
			continue
		# Punctuation does not require translation
		if not set(ascii_letters).intersection(word):
			output.append(word)
			continue

		m = re.match(r'^(?P<pre>[\W]*)(?P<word>.+?)(?P<post>[\W]*)$', word)
		d = m.groupdict()

		i = 0
		word = d['word']
		while len(word) > i:
			if word[i] in vowels:
				break
			if i > 0 and word[i] in 'yY':
				break
			i += 1
		d['fore'] = word[i:]
		d['aft'] = word[:i]
		new_word = '%(pre)s%(fore)s-%(aft)say%(post)s' % d
		output.append(new_word)
	return ''.join(output)


if __name__ == '__main__':
	main()
