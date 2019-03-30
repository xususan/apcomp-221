#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-18
@author samuelclay
"""

import csv, json, re
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
        if len(row) < 48:
            print(" --->", len(row), "\t", row)
        
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


def count_column_uniques(rows, headers):
    """
    Get the number of unique values in each column of a dataset.
    :param headers: A dictionary of all headers in the file.
    :param rows: A list of lists, representing all rows in the dataset.
    :return: A dictionary of columns with a dictionary of counts of unique column values
    """
    unique_values = {}
    for col in headers:
        unique_values[col] = {}

    for line in rows:
        for index, item in enumerate(line):
            if index >= len(headers): continue
            col_name = headers[index]
            if item in unique_values[col_name]:
                unique_values[col_name][item] += 1
            else:
                unique_values[col_name][item] = 1
    return unique_values


def regex_from_config_file(file_name):
    """
    Read a configuration file that has regex for each column header.
    :param file_name: the name of the configuration file
    :return: a dict of column headers and compiled regex
    """
    fin = open(file_name, 'r')
    
    config = json.loads(fin.read())
    data = {}
    for column, data_regex in config.items():
        data[column] = re.compile(data_regex)
        
    fin.close()
    
    return data
    
    