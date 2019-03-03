#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-03-03
@author samuelclay
Unit tests for k-suppression, k-synthetic, and k-blurring of de-identified data in CSV files.
"""
import pytest
from file_util import count_column_uniques, blur_column, create_bins
from k_suppress import k_suppress

@pytest.fixture
def headers():
    return ['column1', 'column2', 'column3']

@pytest.fixture
def rows():
    return iter([
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


def test_count_columns(rows, headers):
    uniques = count_column_uniques(rows, headers)
    # print(uniques)
    assert uniques == {'column1': {'1': 4, '2': 3, '3': 6, '4': 1}, 
                       'column2': {'2': 7, '1': 3, '3': 3, '5': 1}, 
                       'column3': {'3': 4, '1': 6, '2': 3, '6': 1}}

def test_k_suppress(rows, headers):
    delete_columns = ['column1']
    qi_columns = ['column3']
    out_filename = 'test.csv'
    k = 3
    output_csv = k_suppress(headers, rows, delete_columns, qi_columns, out_filename, k)
    print(output_csv)
    assert output_csv == []

def test_blur_column():
    # uniques = count_column_uniques(rows, headers)
    # blurred = blur_column("column1", 4, uniques)
    # print(blurred)
    pass


def test_create_bins():
    uniques = count_column_uniques(rows, headers)
    print(create_bins(1, uniques['column1']))

