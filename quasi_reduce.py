#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-24
@author Sam
Reads a CSV and rewrites it using only specified fields from a config file.
"""
import sys, csv
from file_util import columns_from_config_file, read_csv, write_csv_to_file

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python quasi_reduce.py infile.csv outfile.csv configfile')
        sys.exit(1)

    headers, rows = read_csv(sys.argv[1])
    out_filename = sys.argv[2]
    delete_columns, qi_columns = columns_from_config_file(sys.argv[3])
    
    # Write only headers found in configfile
    output_csv = []
    output_csv.append([])
    for header in headers:
        if header not in delete_columns:
            output_csv[0].append(header)

    # Rewrite each line, only keep columns with headers found in configfile
    for line in rows:
        output_csv.append([])
        for i, item in enumerate(line):
            if headers[i] not in delete_columns:
                output_csv[-1].append(item)
    
    # Save rewritten CSV to outfile
    write_csv_to_file(output_csv, out_filename)

    remaining_column_count = len(headers) - len(delete_columns) - len(qi_columns)
    print(" ---> Wrote {} lines with {}+{}/{} columns to {}.".format(len(output_csv), 
                                                                     len(qi_columns), 
                                                                     remaining_column_count, 
                                                                     len(headers), 
                                                                     sys.argv[2]))
