#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-03-03
@author samuelclay
Unit tests for k-suppression, k-synthetic, and k-blurring of de-identified data in CSV files.
"""
import pytest
from deidentifier_util import count_column_uniques, blur_column, create_bins
from k_suppress import k_suppress
from k_synthetic import k_synthetic
from k_blur import k_blur
from l_diversity import l_diversity
from pprint import pprint

@pytest.fixture
def headers():
    return ['column1', 'column2', 'column3']

@pytest.fixture
def rows():
    return [
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
        ["4", "5", "6"],
        ["7", "7", "7"],
    ]


def test_count_columns(rows, headers):
    uniques = count_column_uniques(rows, headers)
    pprint(uniques)
    assert uniques == {'column1': {'1': 4, '2': 3, '3': 6, '4': 2, '7': 1},
                       'column2': {'1': 3, '2': 7, '3': 3, '5': 2, '7': 1},
                       'column3': {'1': 6, '2': 3, '3': 4, '6': 2, '7': 1}}

def test_k_suppress(rows, headers):
    delete_columns = ['column1']
    qi_columns = ['column3']
    out_filename = 'output/test.csv'
    
    k = 2
    output_csv = k_suppress(headers, rows, delete_columns, qi_columns, out_filename, k)
    pprint(output_csv)
    assert output_csv == [['column1', 'column2', 'column3'],
                          ['1', '2', '3'],
                          ['1', '1', '1'],
                          ['1', '1', '1'],
                          ['1', '1', '1'],
                          ['2', '2', '2'],
                          ['2', '2', '2'],
                          ['2', '2', '2'],
                          ['3', '3', '3'],
                          ['3', '3', '3'],
                          ['3', '3', '3'],
                          ['3', '2', '1'],
                          ['3', '2', '1'],
                          ['3', '2', '1'],
                          ['4', '5', '6'],
                          ['4', '5', '6']]
                          

    k = 3
    output_csv = k_suppress(headers, rows, delete_columns, qi_columns, out_filename, k)
    pprint(output_csv)
    assert output_csv == [['column1', 'column2', 'column3'],
                          ['1', '2', '3'],
                          ['1', '1', '1'],
                          ['1', '1', '1'],
                          ['1', '1', '1'],
                          ['2', '2', '2'],
                          ['2', '2', '2'],
                          ['2', '2', '2'],
                          ['3', '3', '3'],
                          ['3', '3', '3'],
                          ['3', '3', '3'],
                          ['3', '2', '1'],
                          ['3', '2', '1'],
                          ['3', '2', '1']]

def test_k_synthetic(rows, headers):
    delete_columns = ['column1']
    qi_columns = ['column3']
    out_filename = 'output/test.csv'
    
    k = 2
    assert len(rows) == 16
    output_csv = k_synthetic(headers, rows, delete_columns, qi_columns, out_filename, k)
    pprint(output_csv)
    assert len(output_csv) == 18
                          

    k = 3
    output_csv = k_synthetic(headers, rows, delete_columns, qi_columns, out_filename, k)
    pprint(output_csv)
    assert len(output_csv) == 20

def test_k_blur(rows, headers):
    blur_columns = ['column1']
    generalize_columns = ['column3']
    out_filename = 'output/test.csv'
    
    k = 2
    assert len(rows) == 16
    output_csv = k_blur(headers, rows, blur_columns, generalize_columns, out_filename, k)
    pprint(output_csv)
    assert len(output_csv) == 17
                          

    k = 3
    output_csv = k_blur(headers, rows, blur_columns, generalize_columns, out_filename, k)
    pprint(output_csv)
    assert len(output_csv) == 17
    
def test_l_diversity(rows, headers):
    delete_columns = ['column1']
    qi_columns = ['column3']

    counter = l_diversity(headers, rows, delete_columns, qi_columns)
    pprint(counter)
    assert counter[1] == 3
    assert counter[2] == 2
    
def test_blur_column(rows, headers):
    uniques = count_column_uniques(rows, headers)
    bins_1 = create_bins(1, uniques['column1'])
    blurred = blur_column("column1", "4", bins_1)
    assert(blurred == "4")
    bins_2 = create_bins(2, uniques['column1'])
    blurred = blur_column("column1", "7", bins_2)
    assert(blurred == "4")

def test_create_bins(rows, headers):
    uniques = count_column_uniques(rows, headers)
    assert(create_bins(1, uniques['column1']) == ['1', '2', '3', '4', '7'])
    assert(create_bins(2, uniques['column1']) == ['1', '2', '3', '4'])