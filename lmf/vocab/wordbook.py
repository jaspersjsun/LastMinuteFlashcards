#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Description : Word Book
    Author      : FakeCola
    Date        : Jul 25, 2018
"""

import os
import shutil
import codecs
import cPickle as pickle
import logging

from flashcard import Flashcard
from wordlist import WordList


DUMP_SUFFIX = '.dump'
BOOK_STRUCTURE_FNAME = 'book_structure.txt'


# get last modified time of file
get_file_mtime = lambda x: os.stat(x).st_mtime


class WordBook(object):

    def __init__(self, book_home, dump_home, book_name):
        self.book_name = book_name
        self.book_dir = os.path.join(book_home, book_name)
        self.dump_dir = os.path.join(dump_home, book_name)
        self.wordlists = None       # name of wordlist in order
        self.wordlist_dict = None
        self.load_wordbook()

    def load_wordbook(self, reload=False):
        if reload:
            # delete cache
            shutil.rmtree(self.dump_dir)
            logging.info("[reloading] WordBook '%s'..." % self.book_name)

        self.wordlists = list()
        self.wordlist_dict = dict()
        # using book-structure to load wordlists
        with codecs.open(os.path.join(self.book_dir, BOOK_STRUCTURE_FNAME), 'r', 'utf-8') as fin:
            self.structure = dict(map(lambda x: x.strip().split(' '), fin.readlines()))
        for name, fname in self.structure.iteritems():
            self.wordlists.append(name)
            self.wordlist_dict[name] = self.load_wordlist(name, fname)

        if reload:
            logging.info("[reloaded] WordBook '%s'" % self.book_name)
        else:
            logging.info("[loaded] WordBook '%s'" % self.book_name)

    def reload_workbook(self):
        self.load_wordbook(reload=True)

    def load_wordlist(self, name, fname):
        wordlist_fname = os.path.join(self.book_dir, fname)
        dump_fname = os.path.join(self.dump_dir, fname + DUMP_SUFFIX)
        if os.path.exists(dump_fname) and \
                get_file_mtime(dump_fname) > get_file_mtime(wordlist_fname):
            # load from cache
            with open(dump_fname, 'rb') as pickle_file:
                wordlist = pickle.load(pickle_file)
        else:
            # load from original file and dump
            if os.path.exists(dump_fname):
                logging.info("[parsing] File modification detected, re-parse '%s'" % wordlist_fname)
            else:
                logging.info("[parsing] '%s'" % wordlist_fname)
            wordlist = WordList(name, wordlist_fname)
            dump_path = os.path.dirname(dump_fname)
            if not os.path.exists(dump_path):
                os.makedirs(dump_path)
            with open(dump_fname, 'wb') as pickle_file:
                pickle.dump(wordlist, pickle_file)
        logging.info("[loaded] WordList '%s'" % name)
        return wordlist




