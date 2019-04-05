#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-03-03
@author xususan
Unit tests for k-suppression, k-synthetic, and k-blurring of de-identified data in CSV files.
"""
import pytest
from clean_csv import deduplicate
from pprint import pprint
from file_util import read_csv, regex_from_config_file

@pytest.fixture
def headers():
    return ['column1', 'column2', 'completed']

@pytest.fixture
def rows():
    return [
        ["1", "2", "3"],
        ["1", "1", "1", "2"],
        ["1", "1", "1"],
        ["1", "1", "1"],
        ["2", "2"],
        ["2", "2", "2"],
        ["2", "2", "2"],
        ["3", "3", "3"],
        ["3", "3", "2"],
        ["3", "3", "3"],
        ["3", "2", "1"],
        ["3", "2", "1"],
        ["3", "2", "1"],
        ["4", "5", "6"],
        ["4", "5", "6"],
        ["7", "7", "7"],
    ]


def test_deduplicate(rows, headers):
    deduplicated = deduplicate(rows, headers)
    pprint(deduplicated)
    assert deduplicated == [
        ['column1', 'column2', 'maybe_completed'],
        ["1", "2", "3"],
        ["1", "1", "1"],
        ["2", "2", "2"],
        ["3", "3", "3"],
        ["3", "2", "1"],
        ["4", "5", "6"],
        ["7", "7", "7"],
    ]

def test_type_checks():
    filename = 'output/clean.csv'
    config_file = 'config/type_checks.json'
    headers, rows = read_csv(filename=filename)
    regex_checks = regex_from_config_file(config_file)
    
    mismatched_count = 0
    unchecked_columns = set()
    for row in rows:
        for i, column in enumerate(row):
            if headers[i] not in regex_checks:
                if headers[i] not in unchecked_columns:
                    unchecked_columns.add(headers[i])
                    print(" ---> No type check for {}: {}".format(headers[i], column))
                continue
            if not regex_checks[headers[i]].match(column):
                print(" ---> Mismatch on {}: {} {}".format(headers[i], column, row))
                mismatched_count += 1
    
    print(" ---> Mismatched count: {}".format(mismatched_count))
    assert mismatched_count == 0