#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-24
@author Sam
Reads a CSV and rewrites it using only specified fields from a config file.
"""
import sys, csv
from file_util import read_int_config_file

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python organize.py infile.csv outfile.csv configfile')
        sys.exit(1)

    fin = open(sys.argv[1], 'r')
    csv_in = csv.reader(fin)
    headers = next(csv_in)
    
    keep_headers = read_int_config_file(sys.argv[3])

    output_csv = []
    output_csv.append([])
    for h, header in enumerate(headers):
        if h in keep_headers:
            output_csv[0].append(header)

    for line in csv_in:
        output_csv.append([])
        for i, item in enumerate(line):
            if i in keep_headers:
                output_csv[-1].append(item)
    
    with open(sys.argv[2], 'w') as outfile:
        writer = csv.writer(outfile)
        for row in output_csv:
            writer.writerow(row)

    print(f" ---> Wrote {len(output_csv)} lines with {len(headers)} columns to {sys.argv[2]}.")

    fin.close()