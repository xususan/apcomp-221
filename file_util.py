#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-18
@author waldo
@maintainer samuelclay
"""


def read_int_config_file(file_name):
    """
    Read a configuration file that is a csv where the first entry in each line is a 
    header column name. Returns a list of columns.
    :param file_name: the name of the configuration file
    :return: a sorted list of header columns that were in the file
    """
    fin = open(file_name, 'r')
    ret_l = []
    for l in fin:
        try:
            ret_l.append(l.split(',')[0].strip())
        except:
            continue
    fin.close()
    return sorted(ret_l)