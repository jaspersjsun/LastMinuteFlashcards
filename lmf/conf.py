#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Description : Config file
    Author      : FakeCola
    Date        : Jul 25, 2018
"""

from __future__ import print_function

import os
import argparse


LOG_PATH = '../log/'
LOG_FORMAT = '%(filename)s [%(asctime)s] [%(levelname)s] %(message)s'

# directory to store all the books
BOOK_HOME = '../vocab'

# directory to store book caches
DUMP_HOME = os.path.join(BOOK_HOME, '.auto_dump')

# selected book for default loading
SELECTED_BOOK = 'LastMinuteVocabulary2017'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("variable_name", type=str,
                        help="variable name to fetch its value")
    args = parser.parse_args()

    print(globals()[args.variable_name])
