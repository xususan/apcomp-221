#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-03-30
@author xususan

Removes duplicates from CSV and writes to file.

"""
import sys
from collections import Counter
from file_util import read_csv, write_csv_to_file
   
def deduplicate(rows, headers): 
    """
    Given a CSV reader, deduplicates values based on identifiers.

    :param rows: rows of column arrays
    :param headers: row with column names
    :return: a list to write to CSV with deduplicated entries.
    """
    
    # Move 'completed' header to the end because that's where the data is
    MISPLACED_COLUMN = 'completed'
    completed_index = headers.index(MISPLACED_COLUMN)
    headers.pop(completed_index)
    headers.append(MISPLACED_COLUMN)
    
    # Write headers to file
    output_csv = [[]]
    for header in headers:
        output_csv[0].append(header)

    n_cols = len(headers)

    deduplicated_values = {}
    # Keep count of how many times a given set of identifiers have shown up
    counter = Counter()
    for line in rows:
        identifiers = ','.join(line[:2])
        # Update the count of identifiers by 1
        counter.update({identifiers, 1})

        # Only write to file the first time we see a pair of identifiers
        if counter[identifiers] == 1:
            deduplicated_values[identifiers] = line   

        if counter[identifiers]:
            if (len(deduplicated_values[identifiers]) != n_cols and len(line) == n_cols) or (
                len(deduplicated_values[identifiers]) < len(line) and len(line) <= n_cols) or (
                len(deduplicated_values[identifiers]) > n_cols):
                deduplicated_values[identifiers] = line

    for line in deduplicated_values.values():
        output_csv.append(line)

    return output_csv

def remove_rows_with_missing(output_csv):
    """
    Split CSV into a corrupt and non-corrupt CSV based on number of columns.

    :param output_csv: Iterator over header and rows of a CSV
    :return: tuple, where the first entry is the non-corrupt CSVs and the second entry is the corrupt CSV
    """
    headers = output_csv[0]
    rows = output_csv[1:]
    n_cols = len(headers)

    corrupt_csv = []
    corrupt_csv.append(headers)

    non_corrupt_csv = []
    non_corrupt_csv.append(headers)

    for line in rows:
        if len(line) != n_cols:
            corrupt_csv.append(line)
        else:
            non_corrupt_csv.append(line)

    return non_corrupt_csv, corrupt_csv


    
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python clean_csv.py infile.csv outfile.csv')
        sys.exit(1)
    
    headers, rows = read_csv(filename=sys.argv[1])
    out_non_corrupt_filename = sys.argv[2]
    out_corrupt_filename = out_non_corrupt_filename[:-4] + '_corrupt.csv'

    output_csv = deduplicate(rows, headers)
    non_corrupt_csv, corrupt_csv = remove_rows_with_missing(output_csv)
    write_csv_to_file(non_corrupt_csv, out_non_corrupt_filename)
    write_csv_to_file(corrupt_csv, out_corrupt_filename)





