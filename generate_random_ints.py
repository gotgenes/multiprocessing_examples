#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# generate_random_ints.py
"""Generates a series of random integers as a CSV file.

NOTE: Uses numpy for effeciently generating many numbers.
"""

NUM_COLS = 100
NUM_ROWS = 500000
OUTFILE_NAME = 'random_ints.csv'

import numpy
import optparse
import sys

def make_cli_parser():
    """Make the command line interface parser."""
    usage = "\n\n".join(["python %prog",
            __doc__])
    cli_parser = optparse.OptionParser(usage)
    cli_parser.add_option('-c', '--columns', type='int',
            default=NUM_COLS,
            help="Number of rows to generate [DEFAULT: %default]")
    cli_parser.add_option('-r', '--rows', type='int',
            default=NUM_ROWS,
            help="Number of rows to generate [DEFAULT: %default]")
    cli_parser.add_option('-o', '--outfile',
            default=OUTFILE_NAME,
            help="file for output [DEFAULT: %default]")
    return cli_parser


def main(argv):
    cli_parser = make_cli_parser()
    opts, args = cli_parser.parse_args(argv)
    outfile = open(opts.outfile, 'w')
    integers = numpy.random.random_integers(0, 9, (opts.rows,
        opts.columns))
    numpy.savetxt(outfile, integers, fmt="%d", delimiter=',')


if __name__ == '__main__':
    main(sys.argv[1:])
