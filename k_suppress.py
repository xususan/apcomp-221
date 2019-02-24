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

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python k_suppress.py infile.csv outfile.csv k')
        sys.exit(1)

    fin = open(sys.argv[1], 'r')
    csv_in = csv.reader(fin)
    row_count = sum(1 for row in csv_in)
    fin.seek(0)
    k = int(sys.argv[3])
    headers = next(csv_in)

    print(f" ---> Read {row_count} lines with {len(headers)} columns.")
    sys.stdout.flush()
    
    # Write headers
    output_csv = []
    output_csv.append([])
    for h, header in enumerate(headers):
        output_csv[0].append(header)
    
    # Count each tuple row
    counter = Counter()
    for line in csv_in:
        h = hashlib.md5()
        h.update(','.join(line).encode('utf-8'))
        counter.update([h.hexdigest()])
    
    # Second pass through data, only keeping rows with unique counts > k
    fin.seek(0)
    next(csv_in)
    output_csv = []
    for line in csv_in:
        h = hashlib.md5()
        h.update(','.join(line).encode('utf-8'))
        if counter[h.hexdigest()] > k:
            output_csv.append(line)
        
    # Save rewritten CSV to outfile
    with open(sys.argv[2], 'w') as outfile:
        writer = csv.writer(outfile)
        for row in output_csv:
            writer.writerow(row)

    print(f" ---> Wrote {len(output_csv)} lines with {len(headers)} columns and k = {k} to {sys.argv[2]}.")

    fin.close()