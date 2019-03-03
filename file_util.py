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
    :return: a tuple of deleted columns, quasi-identifier columns, and 
             columns to keep, each as a list of header names as strings
    """
    fin = open(file_name, 'r')
    
    if not columns:
        columns = ['delete_columns', 'quasi_identifiers']
    
    config = json.loads(fin.read())
    delete_columns = [value.strip() for value in config["delete_columns"]]
    quasi_identifiers = [value.strip() for value in config["quasi_identifiers"]]
    generalize_columns = [value.strip() for value in config["generalize_columns"]]
    blur_columns = [value.strip() for value in config["blur_columns"]]

    fin.close()
    
    locals_ = locals()
    values = tuple([sorted(locals_[c]) for c in columns])
    
    return values
    
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

def blur_entry(column_name, value):
    """Blurs entry for a column.
    """
    return value
    