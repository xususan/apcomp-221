#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-03-30
@author samuelclay

Removes

"""
import sys
import pdb
from collections import defaultdict, Counter
from file_util import read_csv, write_csv_to_file
    
    
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python clean_csv.py infile.csv outfile.csv')
        sys.exit(1)
    
    headers, rows = read_csv(filename=sys.argv[1])
    out_filename = sys.argv[2]

    # Write headers to file
    output_csv = [[]]
    for header in headers:
        output_csv[0].append(header)

    # Keep count of how many times a given 
    counter = Counter()
    for line in rows:
        identifiers = ','.join(line[:2])
        counter.update({identifiers, 1})
        if counter[identifiers] == 1:
        	output_csv.append(line)

    write_csv_to_file(output_csv, out_filename)





