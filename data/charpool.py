# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 18:57:39 2014

@author: steven_c
"""


literals = ['\\', "\'", '\"', '\a', '\b', '\f', '\n', '\r', '\t', '\b']


vowels = ['a', 'e', 'i', 'o', 'u']

sentenceends = ['.', '!', '?']


punctuation = ['.', '!', '?', ',', ';', ':', '"', "'"]


contractions = [(r'won\'t', 'will not'),
                (r'can\'t', 'cannot'),
                (r'i\'m', 'i am'),
                (r'ain\'t', 'is not'),
                (r'(\w+)\'ll', '\g<1> will'),
                (r'(\w+)n\'t', '\g<1> not'),
                (r'(\w+)\'ve', '\g<1> have'),
                (r'(\w+)\'s', '\g<1> is'),
                (r'(\w+)\'re', '\g<1> are'),
                (r'(\w+)\'d', '\g<1> would'),
                ]
