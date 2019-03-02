#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-24
@author samuelclay
Reads a CSV and writes out a new CSV with only non-unique rows with at least k elements (k-suppressed)
"""
import sys, csv
import hashlib
from collections import Counter
from file_util import read_csv

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python k_suppress.py infile.csv outfile.csv k')
        sys.exit(1)
    
    headers, rows = read_csv(filename=sys.argv[1])
    k = int(sys.argv[3])
    
    # Write headers
    output_csv = []
    output_csv.append([])
    for h, header in enumerate(headers):
        output_csv[0].append(header)
    
    # Count each tuple row
    counter = Counter()
    for line in rows:
        h = hashlib.md5()
        h.update(','.join(line).encode('utf-8'))
        counter.update([h.hexdigest()])
    
    # Second pass through data, only keeping rows with unique counts > k
    output_csv = []
    for line in rows:
        h = hashlib.md5()
        h.update(','.join(line).encode('utf-8'))
        if counter[h.hexdigest()] > k:
            output_csv.append(line)
        
    # Save rewritten CSV to outfile
    with open(sys.argv[2], 'w') as outfile:
        writer = csv.writer(outfile)
        for row in output_csv:
            writer.writerow(row)

    print(" ---> Wrote {} lines with {} columns and k = {} to {}.".format(len(output_csv), 
                                                                         len(headers), k, 
                                                                         sys.argv[2]))