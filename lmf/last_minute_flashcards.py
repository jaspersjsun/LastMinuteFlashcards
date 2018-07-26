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
from termcolor import colored

import conf
from vocab.wordbook import WordBook
from player.listplayer import ListPlayer
from window.mainwindow import MainWindow


LOG_FILE = conf.LOG_PATH + 'lmf.log'
LOG_FORMAT = conf.LOG_FORMAT
BOOK_HOME = conf.BOOK_HOME
DUMP_HOME = conf.DUMP_HOME
SELECTED_BOOK = conf.SELECTED_BOOK


COMMANDS = {    # Key-command mapping
    '\x1a': 'ABORT',    # Ctrl-z
    '\x03': 'ABORT',    # Ctrl-c
    '\x04': 'ABORT',    # Ctrl-d
    'q': 'QUIT',
    '\x1b\x1b': 'QUIT',     # ESC Key (twice)
    'j': 'PREVIOUS',
    'h': 'PREVIOUS',
    'p': 'PREVIOUS',
    '\x1b[D': 'PREVIOUS',   # left arrow
    '\x1b[A': 'PREVIOUS',   # up arrow
    'k': 'NEXT',
    'l': 'NEXT',
    ' ': 'NEXT',
    'n': 'NEXT',
    '\x1b[C': 'NEXT',   # right arrow
    '\x1b[B': 'NEXT',   # down arrow
    'y': 'CONFIRM',
    '\r': 'CONFIRM',    # Enter Key
    'r': 'RELOAD',
}

class LastMinuteFlashcards(object):

    def __init__(self):
        self.mainwin = MainWindow()
        self.wordbook = WordBook(BOOK_HOME, DUMP_HOME, SELECTED_BOOK)
        self.selected_list_idx = 0

    def reload_wordbook(self):
        self.wordbook.reload_wordbook()

    def get_selected_wordlist_name(self):
        return self.wordbook.wordlists[self.selected_list_idx]

    def draw_main_page(self):
        self.mainwin.new_page()
        self.mainwin.screen_show(self.wordbook.wordlists)
        self.mainwin.screen_show(colored(">>>>>> %s <<<<<<" % self.wordbook.book_name,
                'magenta', attrs=['bold']))
        self.mainwin.screen_show("\nAvaliable wordlists:")
        selected_wordlist_name = self.get_selected_wordlist_name()
        for listname in self.wordbook.wordlists:
            if listname != self.get_selected_wordlist_name():
                self.mainwin.screen_show(colored('  * ', 'red') + listname)
            else:
                self.mainwin.screen_show(colored(u'  \u2192 ', 'green') +
                        colored(listname, 'green', attrs=['bold']))
        self.mainwin.screen_show(colored("\nPress 'j', 'k' to select list", 'cyan'))
        self.mainwin.screen_show(colored("Press 'y' to confirm", 'cyan'))
        self.mainwin.screen_show(colored("Press 'q' to quit", 'cyan'))

    def learn_wordlist(self):
        wordlist_name = self.get_selected_wordlist_name()
        self.player = ListPlayer(self.wordbook.wordlist_dict[wordlist_name], self.mainwin)
        self.player.play()

    def run(self):
        while True:
            self.draw_main_page()
            pressed_key = readchar.readkey()
            if pressed_key not in COMMANDS:
                logging.warn("key '%s' can not be recognized" % repr(pressed_key))
                continue
            # else
            cmd = COMMANDS[pressed_key]

            if cmd == 'ABORT':
                self.mainwin.close()
                raise KeyboardInterrupt

            elif cmd == 'QUIT':
                self.mainwin.close()
                logging.info("Bye bye")
                break

            elif cmd == 'PREVIOUS':
                self.selected_list_idx = (self.selected_list_idx - 1) % len(self.wordbook.wordlists)
                self.draw_main_page()

            elif cmd == 'NEXT':
                self.selected_list_idx = (self.selected_list_idx + 1) % len(self.wordbook.wordlists)
                self.draw_main_page()

            elif cmd == 'CONFIRM':
                self.learn_wordlist()

            elif cmd == 'RELOAD':
                self.reload_wordbook()
                self.selected_list_idx = 0
                self.draw_main_page()


def main(reload):
    lmf = LastMinuteFlashcards()
    if reload:
        lmf.reload_wordbook()
    lmf.run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--reload", help="reload the vocabulary", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, filename=LOG_FILE, format=LOG_FORMAT)
    logging.warning("\n\n-------------------- start -----------------------\n")

    main(args.reload)
