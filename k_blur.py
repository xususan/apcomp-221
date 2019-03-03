#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-03-03
@author samuelclay
Reads a CSV and writes out a new CSV with all columns that have fewer than k unique values blurred.
Outputted dataset must still be run through a k-suppression to be fully k-anonymous. This script
just makes the k-suppression have to do less work and suppress fewer values.
"""
import sys
from collections import defaultdict
from file_util import columns_from_config_file, read_csv, write_csv_to_file, blur_column, generalize_column, count_column_uniques

    
if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python k_blur.py infile.csv configfile outfile.csv k')
        sys.exit(1)
    
    headers, rows = read_csv(filename=sys.argv[1])
    blur_columns, generalize_columns = columns_from_config_file(sys.argv[2], 
                                                                columns=['blur_columns',
                                                                         'generalize_columns'])
    out_filename = sys.argv[3]
    k = int(sys.argv[4])
    
    # Write headers
    output_csv = [[]]
    for header in headers:
        output_csv[0].append(header)

    unique_values = count_column_uniques(rows, headers)

    bins = {}
    for column in blur_columns:
        bins[column] = create_bins(10, unique_values[column])
    
    # Second pass through data, only keeping rows with unique counts > k
    for line in rows:
        output_csv.append([])
        for i, item in enumerate(line):
            if headers[i] in blur_columns:
                blurred_column = blur_column(headers[i], item, bins[column])
                output_csv[-1].append(blurred_column)
            elif headers[i] in generalize_columns:
                generalized_column = generalize_column(headers[i], item, unique_values, 10)
                output_csv[-1].append(generalized_column)        
    
    # Save rewritten CSV to outfile
    write_csv_to_file(output_csv, out_filename)
    
    print(" ---> Wrote {} lines with {} columns and k = {} to {}.".format(len(output_csv), 
                                                                          len(headers), 
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