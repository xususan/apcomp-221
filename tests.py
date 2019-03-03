#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-03-03
@author samuelclay
Unit tests for k-suppression, k-synthetic, and k-blurring of de-identified data in CSV files.
"""
from file_util import *
from file_util import count_column_uniques
from k_suppress import k_suppress

headers = ['column1', 'column2', 'column3']
rows = iter([
    ["1", "2", "3"],
    ["1", "1", "1"],
    ["1", "1", "1"],
    ["1", "1", "1"],
    ["2", "2", "2"],
    ["2", "2", "2"],
    ["2", "2", "2"],
    ["3", "3", "3"],
    ["3", "3", "3"],
    ["3", "3", "3"],
    ["3", "2", "1"],
    ["3", "2", "1"],
    ["3", "2", "1"],
    ["4", "5", "6"],
])


def test_count_columns():
    uniques = count_column_uniques(rows, headers)
    # print(uniques)
    assert uniques == {'column1': {'1': 4, '2': 3, '3': 6, '4': 1}, 
                       'column2': {'2': 7, '1': 3, '3': 3, '5': 1}, 
                       'column3': {'3': 4, '1': 6, '2': 3, '6': 1}}

def test_k_suppress():
    delete_columns = ['column1']
    qi_columns = ['column3']
    out_filename = 'test.csv'
    k = 3
    output_csv = k_suppress(headers, rows, delete_columns, qi_columns, out_filename, k)
    
    assert output_csv == []

def test_blur_column():
    # blurred = blur_column("column1", 4, rows, headers)
    pass