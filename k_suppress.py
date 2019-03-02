#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-24
@author samuelclay
Reads a CSV and writes out a new CSV with only non-unique rows with at least k elements (k-suppressed)
"""
import sys, csv
import hashlib
from collections import Counter, defaultdict
from file_util import columns_from_config_file, read_csv, qi_for_line

    
if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python k_suppress.py infile.csv configfile outfile.csv k')
        sys.exit(1)
    
    headers, rows = read_csv(filename=sys.argv[1])
    delete_columns, qi_columns = columns_from_config_file(sys.argv[2])
    out_filename = sys.argv[3]
    k = int(sys.argv[4])
    
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
    with open(out_filename, 'w') as outfile:
        writer = csv.writer(outfile)
        for row in output_csv:
            writer.writerow(row)
    
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