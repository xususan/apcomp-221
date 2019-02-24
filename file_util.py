#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-18
@author waldo
"""


def read_int_config_file(file_name):
    """
    Read a configuration file that is a csv where the first entry in each line is an integer
    If the first element in a line contains something other than
    an integer, it will simply be skipped. Returns a list of integers in ascending order
    :param file_name: the name of the configuration file
    :return: a sorted list of integers that were in the file
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