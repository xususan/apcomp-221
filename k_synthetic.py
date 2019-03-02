#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-18
@author Susan
Make a dataset k-anonymous by adding synthetic records, currently done
by copying the record up to k times.
"""
import random, sys, csv
from collections import Counter
import pdb
import hashlib
from file_util import columns_from_config_file, read_csv, qi_for_line

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python k_synthetic_records.py in_file config_file out_file k')
        sys.exit(1)

    headers, rows = read_csv(filename=sys.argv[1])

    # Get names of columns to delete and quasi identifiers
    delete_columns, qi_columns = columns_from_config_file(sys.argv[2])
    out_filename = sys.argv[3]

    ctr = Counter()
    k = int(sys.argv[4])

    # Write headers
    output_csv = [[]]
    for header in headers:
        output_csv[0].append(header)

    # Read over each line and count how many times they have occurred
    counter = Counter()
    for line in rows:
        h = hashlib.md5()
        qi = qi_for_line(line, qi_columns, headers)
        h.update(','.join(qi).encode('utf-8'))
        counter.update([h.hexdigest()])

    # Second pass: if there are k unique counts, write to dataset
    for line in rows:
        h = hashlib.md5()
        qi = qi_for_line(line, qi_columns, headers)
        h.update(','.join(qi).encode('utf-8'))
        number_of_copies = max(k - counter[h.hexdigest()], 0) + 1
        for _ in range(number_of_copies):
            output_csv.append(line)
            counter.update([h.hexdigest()])


    # Save rewritten CSV to outfile
    with open(out_filename, 'w') as outfile:
        writer = csv.writer(outfile)
        for row in output_csv:
            writer.writerow(row)

    print(" ---> Wrote {} lines for k = {} to {}.".format(len(output_csv),
                                                          k, 
                                                          out_filename))

