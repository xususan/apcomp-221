#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-18
@author Susan
Get the number of unique values in each column of a dataset.
"""
import random, sys, csv

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python get_counts.py file')
        sys.exit(1)

    fin = open(sys.argv[1], 'r')
    csv_in = csv.reader(fin)
    header = next(csv_in)

    unique_values = {}
    for col in range(len(header)):
        unique_values[col] = {}

    for line in csv_in:
        for index, item in enumerate(line):
            if item in unique_values[index]:
                unique_values[index][item] += 1
            else:
                unique_values[index][item] = 1

    for i, col in enumerate(header):
        if len(unique_values[i]) < 20:
            print(col, unique_values[i])


    fin.close()