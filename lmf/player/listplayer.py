#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Description : Play a Word List
    Author      : FakeCola
    Date        : Jul 25, 2018
"""

from __future__ import print_function

import logging
import random

import readchar


POS_TAGS = [    # Part-Of-Speech tags
        'n',
        'adj',
        'v',
]

COMMANDS = {    # Key-command mapping
    '\x1a': 'ABORT',    # Ctrl-z
    '\x03': 'ABORT',    # Ctrl-c
    '\x04': 'ABORT',    # Ctrl-d
    'q': 'QUIT',
    '\x1b\x1b': 'QUIT',     # ESC (twice)
    'j': 'PREVIOUS',
    'p': 'PREVIOUS',
    'k': 'NEXT',
    ' ': 'NEXT',
    'n': 'NEXT',
    'r': 'REPEAT',
    't': 'TEST',        # Toggle: test mode
    's': 'SHUFFLE'      # Toggle: shuffle the order
}


class ListPlayer(object):

    def __init__(self, wordlist, window):
        self.wordlist = wordlist
        self.word_dict = wordlist.word_dict
        self.window = window
        self.screen_show = self.window.screen_show
        self.new_page = self.window.new_page

    def reset_word_idx(self):
        self.word_idx = -1
        self.header = False

    def next(self):
        if self.header:
            self.header = False
            flashcard = self.word_dict[self.words[self.word_idx]]
            flashcard.show_definition(self.screen_show)
            return
        if self.word_idx + 1 < self.word_num:
            self.word_idx += 1
            flashcard = self.word_dict[self.words[self.word_idx]]
            self.new_page()
            if self.test_mode:
                flashcard.show_base(self.screen_show)
                self.header = True
            else:
                flashcard.show(self.screen_show)
        else:
            logging.info("already reach the tail")

    def previous(self):
        if self.word_idx <= 0:
            logging.info("already reach the head")
            return
        else:
            self.word_idx -= 2
            self.header = False
            self.next()

    def start(self):
        print('\n\n--------------- %s : %s ---------------' % (
                self.wordlist.name, 'random' if self.shuffle else 'normal'))
        self.words = list(self.wordlist.words)
        if self.shuffle:
            random.shuffle(self.words)
        self.word_num = len(self.words)
        self.reset_word_idx()
        self.next()

    def abort(self):
        self.window.close()
        logging.info("aborted")
        raise KeyboardInterrupt

    def play(self, test_mode=True, shuffle=False):
        self.test_mode = test_mode
        self.shuffle = shuffle
        self.start()

        while True:
            pressed_key = readchar.readkey()
            if pressed_key not in COMMANDS:
                logging.warn("key '%s' can not be recognized" % repr(pressed_key))
                continue
            # else
            cmd = COMMANDS[pressed_key]
            if cmd == 'ABORT':
                self.abort()
            elif cmd == 'QUIT':
                logging.info("quit current play")
                break
            elif cmd == 'PREVIOUS':
                self.previous()
            elif cmd == 'NEXT':
                self.next()
            elif cmd == 'REPEAT':
                logging.info("start from begining again")
            elif cmd == 'TEST':
                if self.test_mode:
                    self.test_mode = False
                    logging.info("test mode: turn off")
                    if self.header:
                        self.next()
                else:
                    self.test_mode = True
                    logging.info("test mode: turn on")
            elif cmd == 'SHUFFLE':
                self.shuffle = not self.shuffle
                if self.shuffle:
                    logging.info("word order: random")
                else:
                    logging.info("word order: normal")
                self.start()


