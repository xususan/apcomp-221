#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-18
@author Susan
Make a dataset k-anonymous by adding synthetic records, currently done
by randomly sampling from the original dataset.
"""
import sys
from collections import Counter, defaultdict
import hashlib
from file_util import columns_from_config_file, read_csv, write_csv_to_file
from deidentifier_util import qi_for_line, create_synthetic_record

def k_synthetic(headers, rows, delete_columns, qi_columns, out_filename, k):
    """
    :param headers: list of strings with column headers
    :param rows: iter list of rows from csv dataset
    :param delete_columns: list of columns to suppress from output csv
    :param qi_columns: list of columns to count unique values in for synthetic additions
    :param out_filename: string of output csv file name
    :param k: integer of k-anonymity value
    :return: list of list of strings, each list being a row of columns with the first row 
             being header column names
    """
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
        output_csv.append(line)
        number_extra_copies = max(k - counter[h.hexdigest()], 0)
        for _ in range(number_extra_copies):
            new_line = create_synthetic_record(line, qi_columns, headers, rows)
            output_csv.append(new_line)
            counter.update([h.hexdigest()])
        assert(counter[h.hexdigest()] >= k)


    # Save rewritten CSV to outfile
    write_csv_to_file(output_csv, out_filename)

    print(" ---> Wrote {} lines for k = {} to {}.".format(len(output_csv),
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
        print('Usage: python k_synthetic_records.py in_file config_file out_file k')
        sys.exit(1)

    headers, rows = read_csv(filename=sys.argv[1])

    # Get names of columns to delete and quasi identifiers
    delete_columns, qi_columns = columns_from_config_file(sys.argv[2])
    out_filename = sys.argv[3]
    k = int(sys.argv[4])

    k_synthetic(headers, rows, delete_columns, qi_columns, out_filename, k)