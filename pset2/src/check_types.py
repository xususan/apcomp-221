#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-03-30
@author samuelclay

Reads a CSV file and checks each column against a regex to ensure it meets the specified data format.

"""
import sys
from file_util import read_csv, regex_from_config_file
    
    
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python check_types.py infile.csv config.json')
        sys.exit(1)
    
    headers, rows = read_csv(filename=sys.argv[1])
    config_file = sys.argv[2]
    regex_checks = regex_from_config_file(config_file)
    
    mismatched_count = 0
    unchecked_columns = set()
    for row in rows:
        for i, column in enumerate(row):
            if headers[i] not in regex_checks:
                if headers[i] not in unchecked_columns:
                    unchecked_columns.add(headers[i])
                    print(" ---> No type check for {}: {}".format(headers[i], column))
                continue
            if not regex_checks[headers[i]].match(column):
                print(" ---> Mismatch on {}: {} {}".format(headers[i], column, row))
                mismatched_count += 1
    
    print(" ---> Mismatched count: {}".format(mismatched_count))