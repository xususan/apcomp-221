#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-03-03
@author samuelclay
Unit tests for k-suppression, k-synthetic, and k-blurring of de-identified data in CSV files.
"""
from count_column_uniques import count_column_uniques

rows = iter([
    [1, 2, 3],
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
    [3, 2, 1],
    [4, 5, 6],
])

headers = ['column1', 'column2', 'column3']

def test_count_columns():
    uniques = count_column_uniques(rows, headers)

    assert uniques == {'column1': {1: 2, 2: 1, 3: 2, 4: 1}, 
                       'column2': {2: 3, 1: 1, 3: 1, 5: 1}, 
                       'column3': {3: 2, 1: 2, 2: 1, 6: 1}}

def test_blur_column():
    blurred = blur_column("column1", 4, rows, headers):

