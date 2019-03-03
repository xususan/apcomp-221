#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-18
@author Susan
Get the number of unique values in each column of a dataset.
"""
import sys, csv, file_util

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python get_counts.py file config_file')
        sys.exit(1)

    headers, rows = file_util.read_csv(filename=sys.argv[1])

    deleted, qi_columns = file_util.columns_from_config_file(sys.argv[2])

    unique_values = file_util.count_column_uniques(rows, headers)

    # Print out the count of each value for each column for the columns 
    # specified in the config file
    for i, col in enumerate(headers):
        if col in qi_columns:
            print(col, (unique_values[col]))
