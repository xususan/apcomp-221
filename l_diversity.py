#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-18
@author Susan
Count how many records are l-diverse.
"""
import sys
from collections import Counter
from file_util import columns_from_config_file, read_csv
from deidentifier_util import qi_for_line

def l_diversity(headers, rows, delete_columns, qi_columns):
    """
    :param headers: list of strings with column headers
    :param rows: iter list of rows from csv dataset
    :param delete_columns: list of columns to suppress from output csv
    :param qi_columns: list of columns to count unique values in for suppressing
    :return: counter of all possible l-diversity values
    """
    non_identifying_columns = []
    for header in enumerate(headers):
        if header not in qi_columns and header not in delete_columns:
            non_identifying_columns.append(header)


    # Read over each line and count how many times they have occurred
    dictionary_entries = {}

    for line in rows:
        qi = qi_for_line(line, qi_columns, headers)
        h = ','.join(qi)

        if h not in dictionary_entries:
            entries_seen = {key[1]: set([]) for key in non_identifying_columns}
        else:
            entries_seen = dictionary_entries[h]

        for i, column_name in non_identifying_columns:
            entries_seen[column_name].add(line[i])
        dictionary_entries[h] = entries_seen

    # Count all the possible l-diversity values
    counter = Counter()
    for qi, d in dictionary_entries.items():
        for column, l_val in d.items():
            counter.update([len(l_val)])

    print(counter)
    
    return counter
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python l_diversity.py in_file config_file')
        sys.exit(1)

    headers, rows = read_csv(filename=sys.argv[1])

    # Get names of columns to delete and quasi identifiers
    delete_columns, qi_columns = columns_from_config_file(sys.argv[2])

    l_diversity(headers, rows, delete_columns, qi_columns)
    
