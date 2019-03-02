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

    fin = open(sys.argv[1], 'r')
    csv_in = csv.reader(fin)
    header = next(csv_in)

    columns = set(file_util.read_int_config_file(sys.argv[2]))

    # For each column, keep a dictionary of the possible values and their counts
    unique_values = {}
    for col in range(len(header)):
        unique_values[col] = {}

    # Iterate over the file, updating how many times each value has been seen
    for line in csv_in:
        for index, item in enumerate(line):
            if item in unique_values[index]:
                unique_values[index][item] += 1
            else:
                unique_values[index][item] = 1

    # Print out the count of each value for each column for the columns 
    # specified in the config file
    for i, col in enumerate(header):
        if col in columns:
            print(col, unique_values[i])


    fin.close()