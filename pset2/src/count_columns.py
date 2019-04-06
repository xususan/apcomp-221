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

def print_values_by_col(headers, rows, columns_of_interest):
    """Given a CSV, print the distribution of data for columns of interest.

    :param headers: row indicating header array
    :param rows: rows of column arrays
    :return: None
    """
    unique_values = count_column_uniques(rows, headers)
    for col in columns_of_interest:
        print(col)
        od = (OrderedDict((sorted(unique_values[col].items(), key= lambda x: x[0]))))
        for key,value in od.items():
            print("%s \t %d" % (key, value))



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python count_column_uniques.py csv_file')
        sys.exit(1)
        
    headers, rows = read_csv(sys.argv[1])
    column_count = count_columns(rows)

    for col, count in column_count.items():
        print(" --->", col, "\tcolumns,\t", count, "\trows")
    
    total = sum(c for c in column_count.values())
    print(" ---> Total rows:", total)

    headers, rows = read_csv(sys.argv[1])
    unique_values = count_column_uniques(rows, headers)
    print("\n ---> Unique values per column")
    for col, values in unique_values.items():
        print("\t", len(values), "\t", col)
        if len(values) < 10:
            print("\t\t{}".format(values))

    headers, rows = read_csv(sys.argv[1])
    columns_of_interest = [
        "LoE",
        "YoB",
        "gender", 
        "countryLabel", 
        "continent", 
        "un_major_region",
        "un_economic_group",
        "un_developing_nation",
        "un_special_region"
    ]
    print_values_by_col(headers, rows, columns_of_interest)
