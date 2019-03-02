#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-24
@author Sam
Reads a CSV and rewrites it using only specified fields from a config file.
"""
import sys, csv
from file_util import read_int_config_file, read_csv

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python quasi_reduce.py infile.csv outfile.csv configfile')
        sys.exit(1)

    headers, rows = read_csv(sys.argv[1])
    keep_headers = read_int_config_file(sys.argv[3])
    
    # Write only headers found in configfile
    output_csv = []
    output_csv.append([])
    for h, header in enumerate(headers):
        if header in keep_headers:
            output_csv[0].append(header)

    # Rewrite each line, only keep columns with headers found in configfile
    for line in rows:
        output_csv.append([])
        for i, item in enumerate(line):
            if headers[i] in keep_headers:
                output_csv[-1].append(item)
    
    # Save rewritten CSV to outfile
    with open(sys.argv[2], 'w') as outfile:
        writer = csv.writer(outfile)
        for row in output_csv:
            writer.writerow(row)

    print(" ---> Wrote {} lines with {}/{} columns to {}.".format(len(output_csv), 
                                                                  len(keep_headers), 
                                                                  len(headers), 
                                                                  sys.argv[2]))
