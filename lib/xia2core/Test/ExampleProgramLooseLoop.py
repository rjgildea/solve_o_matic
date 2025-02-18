# ExampleProgramLooseLoop.py
#
#   Copyright (C) 2006 CCLRC, Graeme Winter
#
#   This code is distributed under the BSD license, a copy of which is
#   included in the root directory of this package.
#
# 27/MAR/06
#
# An example program to test input, output, job control etc. in the new
# XIA. This one gets stuck in a loose loop.

import time
import sys

__doc__ = '''A small program which will write output to the standard output
every so often, for testing of the XIA core.'''

def ep(message, times, spacing):
    '''Write a message $message to the screen $times times with spacing of
    $spacing seconds. Except never stop.'''

    while True:
        sys.stdout.write('%s\n' % message)
        sys.stdout.flush()
        time.sleep(spacing)

def run():
    ep('Hello, world!', 10, 1)

if __name__ == '__main__':
    run()
