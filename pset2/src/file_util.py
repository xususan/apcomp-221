#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-18
@author samuelclay
"""

import sys, csv, json, random
from collections import defaultdict
from collections import OrderedDict

def count_columns(rows):
    """
    Iterates through rows and keeps counts of number of columns.
    :param rows: rows of column arrays
    :return: a dict of column counts to row counts
    """
    counts = defaultdict(int)
    
    # print(" ---> Counting ", len(rows), " rows")
    for row in rows:
        counts[len(row)] += 1
        
    return OrderedDict(reversed(sorted(counts.items())))
    
def read_csv(filename):
    """
    Reads a CSV and returns headers and rows
    :param filename: name of the CSV file
    :param config: name of the quasi-identifier config file, each line a column name
    :return: A tuple of the following:
        headers: list of column names
        rows: list of rows from the CSV file
    """
    fin = open(filename, 'r')
    csv_in = csv.reader(fin)
    headers = next(csv_in)
    rows = csv_in
    
    return headers, rows

def write_csv_to_file(output_csv, out_filename):
    """
    Writes a CSV file to disk.
    :param output_csv: CSV type from the CSV library
    :param out_filename: String of file name to write to
    """
    with open(out_filename, 'w') as outfile:
        writer = csv.writer(outfile)
        for row in output_csv:
            writer.writerow(row)
