#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-18
@author Sam
Get the number of columns per row in a CSV
"""
import sys
from file_util import read_csv, count_columns
from file_util import count_column_uniques
from pprint import pprint
from collections import OrderedDict

columns_of_interest=["LoE","YoB","gender", "countryLabel", "continent"]

def print_values_by_col(headers, rows):
    unique_values = count_column_uniques(rows, headers)
    for col in columns_of_interest:
        pprint(OrderedDict(reversed(sorted(unique_values[col].items(), key= lambda x: x[0]))))



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python count_column_uniques.py csv_file')
        sys.exit(1)
        
    headers, rows = read_csv(sys.argv[1])
    column_count = count_columns(rows)

    for col, count in column_count.items():
        print(" --->", col, "\tcolumns,\t", count, "\trows")
    
    total = sum(c for c in column_count.values())
    print (" ---> Total:", total)

    headers, rows = read_csv(sys.argv[1])
    unique_values = count_column_uniques(rows, headers)
    for col, values in unique_values.items():
        print(len(values), "\t", col)

    print_values_by_col(headers, rows)