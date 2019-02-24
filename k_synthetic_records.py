#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-18
@author Susan
Make a dataset k-anonymous by adding synthetic records, currently done
by copying the record up to k times.
"""
import random, sys, csv, file_util
from collections import Counter
import pdb

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python k_synthetic_records.py file out_file k')
        sys.exit(1)

    fin = open(sys.argv[1], 'r')
    header = fin.readline()

    fout = open(sys.argv[2], 'w')
    ctr = Counter()

    k = int(sys.argv[3])

    # Read over each line 
    for line in fin.readlines():
        if line in ctr:
            ctr[line] += 1
        else:
            ctr[line] = 1

    for line, count in ctr.items():
        number_of_repeats = max(k, count)
        for _ in range(number_of_repeats):
            fout.write(line)


    fin.close()
    fout.close()