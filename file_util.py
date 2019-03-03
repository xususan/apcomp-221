#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-18
@author samuelclay
"""
import pdb

import sys, csv, json, random

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

def qi_for_line(line, qi_columns, headers):
    """
    Returns a list of quasi identifiers for a given line, in order that they appear.
    :param line: A list of entries, represents one row of a CSV
    :param qi_columns: A list of strings, representing the list of quasi-identifiers
    :param headers: A dictionary of all headers in the file.
    :return: A list of all quasi-identifiers for the line, in order.
    """
    qi = []
    
    for i, item in enumerate(line):
        if headers[i] in qi_columns:
            qi.append(item)
    
    return qi

def split_line(line, qi_columns, id_columns, headers):
    """
    Splits a line into quasi identifiers and regular columns.
    :param line: A list of entries, represents one row of a CSV
    :param qi_columns: A list of strings, representing the list of quasi-identifiers
    :param id_columns: A list of strings, representing the list of identifiers
    :param headers: A dictionary of all headers in the file.
    :return: A tuple, where the first element is a list of all 
        quasi-identifiers for the line, in order; and the second element is a list
        of all regular columns (non-identifying) for the line, in order.
    """
    qi = []
    non_qi = []
    
    for i, item in enumerate(line):
        if headers[i] in qi_columns:
            qi.append(item)
        elif headers[i] not in id_columns:
            non_qi.append(item)
        else:
            continue
    return qi, non_qi

def create_synthetic_record(line, qi_columns, headers, rows):
    """
    Creates a new record that has the same quasi-identifiers as a given line.
    :param line: A list of entries, represents one row of a CSV
    :param qi_columns: A list of strings, representing the list of quasi-identifiers
    :param headers: A dictionary of all headers in the file.
    :param rows: A list of lists, representing all rows in the dataset.
    :return: A list of all quasi-identifiers for the line, in order.
    """
    qi = qi_for_line(line, qi_columns, headers)

    # Get a random row from the dataset
    random_row = random.sample(rows, 1)[0]

    # Replace the quasi-identifiers in that line with the true quasi identifiers
    new_entry = []
    for i, item in enumerate(random_row):
        # Don't replace course id either
        if (headers[i] in qi_columns) or (headers[i] == "course_id"):
            new_entry.append(line[i])
        else:
            new_entry.append(item)

    return new_entry

    