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


def create_bins(min_per_bin, dict_of_values): 
    bins = []
    n_in_bin = 0
    numeric_keys = []

    for key in dict_of_values.keys():
        try:
            float_of_key = float(key)
            numeric_keys.append(key)
        except:
            bins.append(key)

    sorted_keys = sorted(numeric_keys, key= lambda x: float(x))
    for key in sorted_keys:
        n_in_bin += dict_of_values[key]
        if n_in_bin > min_per_bin:
            bins.append(key)
            n_in_bin = 0

    return bins

def count_column_uniques(rows, headers):
    unique_values = {}
    for col in headers:
        unique_values[col] = {}

    for line in rows:
        for index, item in enumerate(line):
            col_name = headers[index]
            if item in unique_values[col_name]:
                unique_values[col_name][item] += 1
            else:
                unique_values[col_name][item] = 1
    return unique_values


def blur_column(column_name, value, count_column_uniques):
    """Blurs entry for a column.
    """

    bins_for_column = create_bins(10, unique_values[column_name])

    value_to_return = bins_for_column[0]
    try:
        numeric_value = float(value)
    except:
        return bins_for_column[0]

    for bin_value in bins_for_column:
        try:
            numeric_bin = float(bin_value)
            if numeric_value >= numeric_bin:
                value_to_return = numeric_bin
            else:
                break
        except:
            continue

    return str(value_to_return)

def generalize_column(column_name, value, count_column_uniques):
    return value
    