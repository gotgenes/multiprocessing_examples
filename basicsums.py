#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# basicsums.py
"""A program that reads integer values from a CSV file and writes out their
sums to another CSV file.
"""

import csv
import optparse
import sys

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
    return cli_parser


def parse_input_csv(csvfile):
    """Parses the input CSV and yields tuples with the index of the row
    as the first element, and the integers of the row as the second
    element.

    The index is zero-index based.

    :Parameters:
    - `csvfile`: a `csv.reader` instance

    """
    for i, row in enumerate(csvfile):
        row = [int(entry) for entry in row]
        yield i, row


def sum_rows(rows):
    """Yields a tuple with the index of each input list of integers
    as the first element, and the sum of the list of integers as the
    second element.

    The index is zero-index based.

    :Parameters:
    - `rows`: an iterable of tuples, with the index of the original row
      as the first element, and a list of integers as the second element

    """
    for i, row in rows:
        yield i, sum(row)


def write_results(csvfile, results):
    """Writes a series of results to an outfile, where the first column
    is the index of the original row of data, and the second column is
    the result of the calculation.

    The index is zero-index based.

    :Parameters:
    - `csvfile`: a `csv.writer` instance to which to write results
    - `results`: an iterable of tuples, with the index (zero-based) of
      the original row as the first element, and the calculated result
      from that row as the second element

    """
    for result_row in results:
        csvfile.writerow(result_row)


def main(argv):
    cli_parser = make_cli_parser()
    opts, args = cli_parser.parse_args(argv)
    if len(args) != 2:
        cli_parser.error("Please provide an input file and output file.")
    infile = open(args[0])
    in_csvfile = csv.reader(infile)
    outfile = open(args[1], 'w')
    out_csvfile = csv.writer(outfile)
    # gets an iterable of rows that's not yet evaluated
    input_rows = parse_input_csv(in_csvfile)
    # sends the rows iterable to sum_rows() for results iterable, but
    # still not evaluated
    result_rows = sum_rows(input_rows)
    # finally evaluation takes place as a chain in write_results()
    write_results(out_csvfile, result_rows)
    infile.close()
    outfile.close()


if __name__ == '__main__':
    main(sys.argv[1:])
