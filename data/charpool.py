# -*- coding: utf-8 -*-
__title__ = 'latinpigsay'
__license__ = 'MIT'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.c.projects@gmail.com'
__created_on__ = '12/3/2014'


literals = ['\\', "\'", '\"', '\a', '\b', '\f', '\n', '\r', '\t', '\b']


vowels = ['a', 'e', 'i', 'o', 'u']

sentenceends = ['.', '!', '?']


punctuation = ['.', '!', '?', ',', ';', ':', '"', "'"]


contractions = [(r'won\'t', 'will not'),
                (r'can\'t', 'cannot'),
                (r'i\'m', 'i am'),
                (r'I\'m', 'I am'),
                (r'ma\'am', 'madam'),
                (r'ain\'t', 'is not'),
                (r'(\w+)\'ll', '\g<1> will'),
                (r'(\w+)n\'t', '\g<1> not'),
                (r'(\w+)\'ve', '\g<1> have'),
                (r'(\w+)\'s', '\g<1> is'),
                (r'(\w+)\'re', '\g<1> are'),
                (r'(\w+)\'d', '\g<1> would'),
                ]
