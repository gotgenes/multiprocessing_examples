#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# multiproc_sums.py
"""A program that reads integer values from a CSV file and writes out their
sums to another CSV file, using multiple processes if desired.
"""

import csv
import multiprocessing
import optparse
import sys

NUM_PROCS = multiprocessing.cpu_count()

def make_cli_parser():
    """Make the command line interface parser."""
    usage = "\n\n".join(["python %prog INPUT_CSV OUTPUT_CSV",
            __doc__,
            """
ARGUMENTS:
    INPUT_CSV: an input CSV file with rows of numbers
    OUTPUT_CSV: an output file that will contain the sums\
"""])
    cli_parser = optparse.OptionParser(usage)
    cli_parser.add_option('-n', '--numprocs', type='int',
            default=NUM_PROCS,
            help="Number of processes to launch [DEFAULT: %default]")
    return cli_parser


def main(argv):
    cli_parser = make_cli_parser()
    opts, args = cli_parser.parse_args(argv)
    if len(args) != 2:
        cli_parser.error("Please provide an input file and output file.")
    infile = open(args[0])
    in_csvfile = csv.reader(infile)
    outfile = open(args[1], 'w')
    out_csvfile = csv.writer(outfile)

    # Parse the input file and add the parsed data to a queue for
    # processing, possibly chunking to decrease communication between
    # processes.

    # Process the parsed data as soon as any (chunks) appear on the
    # queue, using as many processes as allotted by the user
    # (opts.numprocs); place results on a queue for output.
    #
    # Terminate processes when the parser stops putting data in the
    # input queue.

    # Write the results to disk as soon as they appear on the output
    # queue.

    # Ensure all child processes have terminated.

    # Clean up files.
    infile.close()
    outfile.close()


if __name__ == '__main__':
    main(sys.argv[1:])
