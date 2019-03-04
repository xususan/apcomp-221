#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-18
@author samuelclay xususan
"""
import random
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


def create_bins(min_per_bin, dict_of_counts): 
    bins = []
    n_in_bin = 0
    numeric_keys = []

    for key in dict_of_counts.keys():
        if key.isnumeric():
            numeric_keys.append(key)
        else:
            bins.append(key)

    sorted_keys = sorted(numeric_keys, key= lambda x: float(x))

    for key in sorted_keys:
        n_in_bin += dict_of_counts[key]
        if n_in_bin >= min_per_bin:
            bins.append(key)
            n_in_bin = 0

    return bins

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
            col_name = headers[index]
            if item in unique_values[col_name]:
                unique_values[col_name][item] += 1
            else:
                unique_values[col_name][item] = 1
    return unique_values


def blur_column(column_name, value, bins_for_column):
    """
    Blurs entry for a column.
    :param column_name: String, name of the column for which this value belongs.
    :param value: String of int, the value to blur.
    :param bins_for_column: List, the bins with which to blur the value. 
    :return:
    """

    value_to_return = bins_for_column[0]
    try:
        numeric_value = int(value)
    except:
        return bins_for_column[0]

    for bin_value in bins_for_column:
        try:
            numeric_bin = int(bin_value)
            if numeric_value >= numeric_bin:
                value_to_return = numeric_bin
            else:
                break
        except:
            continue

    return str(value_to_return)

def generalize_column(column_name, value, count_column_uniques, min_bin_size):
    """
    Generalizes an entry in a column.
    """
    if count_column_uniques[column_name][value] >= min_bin_size:
        return value
    else:
        return "*"
    