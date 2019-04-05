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

@pytest.fixture
def headers():
    return ['column1', 'column2', 'column3']

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
        ['column1', 'column2', 'column3'],
        ["1", "2", "3"],
        ["1", "1", "1"],
        ["2", "2", "2"],
        ["3", "3", "3"],
        ["3", "2", "1"],
        ["4", "5", "6"],
        ["7", "7", "7"],
    ]