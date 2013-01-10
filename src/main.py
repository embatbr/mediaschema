#!/usr/bin/python3.3
#main.py


import sys

import babel


if __name__ == '__main__':
    if '--translate' in sys.argv:
        index = sys.argv.index('--translate')
        filename = sys.argv[index + 1]
        babel.read(filename)