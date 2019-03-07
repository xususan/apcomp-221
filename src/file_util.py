#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-18
@author samuelclay
"""

import sys, csv, json, random

def columns_from_config_file(file_name, columns=None):
    """
    Read a configuration file that is a csv where the first entry in each line is a 
    header column name.
    :param file_name: the name of the configuration file
    :optional param columns: list, the categories of columns to read from the
        config file. Must 
    :return: a tuple of deleted columns, quasi-identifier columns, and 
             columns to keep, each as a list of header names as strings
    """
    fin = open(file_name, 'r')
    
    if not columns:
        columns = ['delete_columns', 'quasi_identifiers']
    
    config = json.loads(fin.read())
    data = {}
    for key, values in config.items():
        data[key] = sorted(v.strip() for v in values)
        
    fin.close()
    
    return tuple(data[c] for c in columns)
    
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
    
    # rows = []
    # for line in csv_in:
    #     rows.append(line)
    
    # print(" ---> Read {} lines with {} columns.".format(len(rows), len(headers)))
    # sys.stdout.flush()
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
