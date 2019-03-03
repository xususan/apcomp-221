#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-18
@author Susan
Get the number of unique values in each column of a dataset.
"""
import sys
from file_util import read_csv, columns_from_config_file
from deidentifier_util import count_column_uniques

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python count_column_uniques.py file config_file')
        sys.exit(1)
        
    config = sys.argv[2]

    headers, rows = read_csv(sys.argv[1])
    deleted, qi_columns = columns_from_config_file(config)

    unique_values = count_column_uniques(rows, headers)

    for col in qi_columns:
        print(col, unique_values[col])
    