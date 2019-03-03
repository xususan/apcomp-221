#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-24
@author samuelclay
Reads a CSV and writes out a new CSV with only non-unique rows with at least k elements (k-suppressed)
"""
import sys
import hashlib
from collections import Counter, defaultdict
from file_util import columns_from_config_file, read_csv, write_csv_to_file
from deidentifier_util import qi_for_line

def k_suppress(headers, rows, delete_columns, qi_columns, out_filename, k):
    """
    :param headers: list of strings with column headers
    :param rows: iter list of rows from csv dataset
    :param delete_columns: list of columns to suppress from output csv
    :param qi_columns: list of columns to count unique values in for suppressing
    :param out_filename: string of output csv file name
    :param k: integer of k-anonymity value
    :return: list of list of strings, each list being a row of columns with the first row 
             being header column names
    """
    # Write headers
    output_csv = [[]]
    for header in headers:
        output_csv[0].append(header)
    
    # Count each tuple row
    counter = Counter()
    for line in rows:
        h = hashlib.md5()
        qi = qi_for_line(line, qi_columns, headers)
        h.update(','.join(qi).encode('utf-8'))
        counter.update([h.hexdigest()])
    
    # Second pass through data, only keeping rows with unique counts > k
    for line in rows:
        h = hashlib.md5()
        qi = qi_for_line(line, qi_columns, headers)
        h.update(','.join(qi).encode('utf-8'))
        if counter[h.hexdigest()] >= k:
            output_csv.append(line)
        
    # Save rewritten CSV to outfile
    write_csv_to_file(output_csv, out_filename)
    
    remaining_column_count = len(headers) - len(delete_columns)
    print(" ---> Wrote {} lines with {} columns and k = {} to {}.".format(len(output_csv), 
                                                                          remaining_column_count, 
                                                                          k, 
                                                                          out_filename))
    
    total_completed = 0
    course_completion_rates = defaultdict(lambda: defaultdict(int))
    course_student_counts = defaultdict(int)
    for line in output_csv:
        completed = False
        for i, item in enumerate(line):
            if headers[i] == 'completed' and item == "True":
                total_completed += 1
                completed = True
        for i, item in enumerate(line):
            if headers[i] == 'course_id':
                course_student_counts[item] += 1
                course_completion_rates[item]['completed' if completed else 'attempted'] += 1

    completion_rate = total_completed/len(output_csv)
    print(" ---> Completion rate overall: %-7s %s%%" % (len(output_csv), round(completion_rate*100, 2)))
    for course_id, rates in course_completion_rates.items():
        student_count = course_student_counts[course_id]
        completion_rate = rates['completed']/(rates['completed']+rates['attempted'])
        print(" ---> Completion rate for %-30s: %-7s %s%%" % (course_id, student_count, round(completion_rate*100, 2)))
    
    return output_csv
    
if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python k_suppress.py infile.csv configfile outfile.csv k')
        sys.exit(1)
    
    headers, rows = read_csv(filename=sys.argv[1])
    delete_columns, qi_columns = columns_from_config_file(sys.argv[2])
    out_filename = sys.argv[3]
    k = int(sys.argv[4])
    
    k_suppress(headers, rows, delete_columns, qi_columns, out_filename, k)