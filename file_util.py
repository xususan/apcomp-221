#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-18
@author samuelclay
"""

import sys, csv, json

def columns_from_config_file(file_name):
    """
    Read a configuration file that is a csv where the first entry in each line is a 
    header column name.
    :param file_name: the name of the configuration file
    :return: a tuple of deleted columns, quasi-identifier columns, and 
             columns to keep, each as a list of header names as strings
    """
    fin = open(file_name, 'r')
    
    delete_columns = []
    quasi_identifiers = []
    
    config = json.loads(fin.read())
    delete_columns = [value.strip() for value in config["delete_columns"]]
    quasi_identifiers = [value.strip() for value in config["quasi_identifiers"]]

    fin.close()
    
    return sorted(delete_columns), sorted(quasi_identifiers)
    
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
    
    rows = []
    for line in csv_in:
        rows.append(line)
    
    print(" ---> Read {} lines with {} columns.".format(len(rows), len(headers)))
    sys.stdout.flush()
    
    return headers, rows
    