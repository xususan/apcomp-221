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
    
    # Remove the 'registered' header as the data is shifted
    DELETE_COLUMN_HEADER = 'registered'
    completed_index = headers.index(DELETE_COLUMN_HEADER)
    headers.pop(completed_index)
    
    # Add the unknown date header to the end
    headers.append("unknown_date")
    
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
        for i, column in enumerate(line):
            if headers[i] == "gender" and column == "null":
                line[i] = ""
        output_csv.append(line)

    return output_csv

def remove_rows_with_missing_or_corrupt_data(output_csv):
    """
    Split CSV into a corrupt and non-corrupt CSV based on number of columns or rows that have
    a grade set to 0.0 but are marked as completed.

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
        is_missing_grade = False
        is_completed = False
        passing_grade = 0
        for c, column in enumerate(line):
            if headers[c] == "completed" and column == "True":
                is_completed = True
            if headers[c] == "passing_grade":
                passing_grade = column
        if is_completed:
            for c, column in enumerate(line):
                if headers[c] == "grade" and column < passing_grade:
                    is_missing_grade = True

        if len(line) != n_cols or is_missing_grade:
            corrupt_csv.append(line)
        else:
            non_corrupt_csv.append(line)
    
    print(" ---> Removed {} corrupted lines, kept {} lines".format(len(corrupt_csv), len(non_corrupt_csv)))
    return non_corrupt_csv, corrupt_csv

    
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python clean_csv.py infile.csv outfile.csv')
        sys.exit(1)
    
    headers, rows = read_csv(filename=sys.argv[1])
    out_non_corrupt_filename = sys.argv[2]
    out_corrupt_filename = out_non_corrupt_filename[:-4] + '_corrupt.csv'

    output_csv = deduplicate(rows, headers)
    non_corrupt_csv, corrupt_csv = remove_rows_with_missing_or_corrupt_data(output_csv)
    write_csv_to_file(non_corrupt_csv, out_non_corrupt_filename)
    write_csv_to_file(corrupt_csv, out_corrupt_filename)
