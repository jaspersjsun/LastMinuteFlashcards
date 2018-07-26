#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Description : Main window using curses programming
    Author      : FakeCola
    Date        : Jul 26, 2018
"""

from __future__ import print_function

import logging
import curses


class MainWindow(object):

    def __init__(self):
        self.mainwin = curses.initscr()
        self.mainwin.clear()
        self.mainwin.refresh()
        logging.info("main window created")

    def new_page(self):
        self.mainwin.clear()
        self.mainwin.refresh()

    def screen_show(self, text):
        print(text, end='\n\r')
        self.mainwin.refresh()

    def close(self):
        curses.endwin()
        logging.info("main window destroyed")

