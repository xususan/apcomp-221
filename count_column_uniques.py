#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-18
@author Susan
Get the number of unique values in each column of a dataset.
"""
import sys, csv, file_util

def count_column_uniques(csv_in, config):
    """
    Prints out the counts of unique values in each column of a dataset.
    :param csv_in: csv reader file
    """
    header = next(csv_in)
    
    deleted, qi_columns = file_util.columns_from_config_file(config)

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
        if col in qi_columns:
            print(col, unique_values[i])
    
    return unique_values
    
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python count_column_uniques.py file config_file')
        sys.exit(1)
        
    config = sys.argv[2]
    fin = open(sys.argv[1], 'r')
    csv_in = csv.reader(fin)
    
    count_column_uniques(csv_in, config)
    
    fin.close()