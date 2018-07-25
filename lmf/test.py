#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Description : Test script for development
    Author      : FakeCola
    Date        : Jul 25, 2018
"""

from __future__ import print_function

import argparse
import logging

import readchar

import conf
from vocab.wordbook import WordBook
from player.listplayer import ListPlayer


LOG_FILE = conf.LOG_PATH + 'lmf.log'
LOG_FORMAT = conf.LOG_FORMAT
BOOK_HOME = conf.BOOK_HOME
DUMP_HOME = conf.DUMP_HOME
SELECTED_BOOK = conf.SELECTED_BOOK


def main(reload):
    wordbook = WordBook(BOOK_HOME, DUMP_HOME, SELECTED_BOOK)
    if reload:
        wordbook.reload_workbook()
    print(wordbook.wordlists)
    print(wordbook.wordlist_dict['list01'].name)
    print(wordbook.wordlist_dict['list01'].words)
    player = ListPlayer(wordbook.wordlist_dict['list01'])
    player.play()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--reload", help="reload the vocabulary", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, filename=LOG_FILE, format=LOG_FORMAT)
    logging.warning("\n\n-------------------- start -----------------------\n")

    main(args.reload)
