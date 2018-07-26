#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Description : Word List
    Author      : FakeCola
    Date        : Jul 25, 2018
"""

import codecs

from flashcard import Flashcard


class WordList(object):

    def __init__(self, name, wordlist_fname):
        self.name = name
        self.words = list()
        self.word_dict = dict()
        with codecs.open(wordlist_fname, 'r', 'utf-8') as fin:
            word_strs = []
            for line in fin:
                line = line.strip()
                if len(line) == 0:
                    flashcard = Flashcard(word_strs)
                    self.words.append(flashcard.word)
                    self.word_dict[flashcard.word] = flashcard
                    word_strs = []
                else:
                    word_strs.append(line)
            # deal with the last word if no empty line followed
            if len(word_strs) > 0:
                flashcard = Flashcard(word_strs)
                self.words.append(flashcard.word)
                self.word_dict[flashcard.word] = flashcard


