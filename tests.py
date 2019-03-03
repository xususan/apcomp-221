#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-03-03
@author samuelclay
Unit tests for k-suppression, k-synthetic, and k-blurring of de-identified data in CSV files.
"""
from count_column_uniques import count_column_uniques

csv = iter([
    ['column1', 'column2', 'column3'],
    [1, 2, 3],
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3],
    [3, 2, 1],
    [4, 5, 6],
])

def test_count_columns():
    uniques = count_column_uniques(csv, 'quasi.config')

    assert uniques == {0: {1: 2, 2: 1, 3: 2, 4: 1}, 
                       1: {2: 3, 1: 1, 3: 1, 5: 1}, 
                       2: {3: 2, 1: 2, 2: 1, 6: 1}}

