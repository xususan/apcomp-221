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

    Returns a list of rows with entries.
    """
    
    # Move 'completed' header to the end because that's where the data is
    MISPLACED_COLUMN = 'completed'
    completed_index = headers.index(MISPLACED_COLUMN)
    headers.pop(completed_index)
    headers.append("maybe_" + MISPLACED_COLUMN)
    
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

        # print(deduplicated_values)

        if counter[identifiers]:
            if (len(deduplicated_values[identifiers]) != n_cols and len(line) == n_cols) or (
                len(deduplicated_values[identifiers]) < len(line) and len(line) <= n_cols) or (
                len(deduplicated_values[identifiers]) > n_cols):
                deduplicated_values[identifiers] = line

    for line in deduplicated_values.values():
        for i, column in enumerate(line):
            if headers[i] == "gender" and column == "null":
                line[i] = ""
        output_csv.append(line)

    return output_csv

    
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python clean_csv.py infile.csv outfile.csv')
        sys.exit(1)
    
    headers, rows = read_csv(filename=sys.argv[1])
    out_filename = sys.argv[2]

    output_csv = deduplicate(rows, headers)
    write_csv_to_file(output_csv, out_filename)





