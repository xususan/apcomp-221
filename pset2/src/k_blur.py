#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-03-30
@author samuelclay

"""
import sys
from collections import defaultdict
from file_util import columns_from_config_file, read_csv, write_csv_to_file
    


    
if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python k_blur.py infile.csv configfile outfile.csv k')
        sys.exit(1)
    
    headers, rows = read_csv(filename=sys.argv[1])

