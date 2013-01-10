#!/usr/bin/python3.3
#babel.py


"""
Module to deal with .babel files. It has functions to read and write these files
and
"""


import re

from defines import *


"""
Defines the rules to extract tokens from a .babel file.
"""
token_spec =[
    ('COMMENT', r'#.*'),
    ('NEWLINE', r'\n'),
    ('SKIP', r'[ \t]+'),
    ('KEYWORD', r'\$[a-z]+'),
    ('STRING', r'".*"'),
    ('LABEL', r'[a-z]+')
]
token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_spec)
get_token = re.compile(token_regex).match


def scan(string):
    """
    Turns a string into a list of tokens.
    """
    match_obj = get_token(string)
    line = 1
    pos = 0
    ret = []

    while match_obj is not None:
        typ = match_obj.lastgroup
        if typ == 'NEWLINE':
            line = line + 1
        elif typ not in ('COMMENT', 'SKIP', 'NEWLINE'):
            val = match_obj.group(typ)
            if typ == 'STRING':
                val = val[1:-1]

            ret.append((typ, val))

        pos = match_obj.end()
        match_obj = get_token(string, pos)

    if pos != len(string):
        raise RuntimeError('Unexpected token \'%s\' in line %s' % (string[pos],
                           line))

    return ret

def read(filename):
    """
    Reads a .babel file and returns a list of BabelFish objects.
    """
    f = open('%s/files/%s.babel' % (projdir, filename))
    string = f.read()
    tokens = scan(string)
    for t in tokens:
        print(t)