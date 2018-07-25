#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Description : Flashcard structure
    Author      : FakeCola
    Date        : Jul 25, 2018
"""

from __future__ import print_function

from termcolor import colored


POS_TAGS = [    # Part-Of-Speech tags
        'n',
        'adj',
        'v',
]


class Definition(object):

    def __init__(self, def_str):
        fields = def_str.split('. ')
        pos_tags = []
        # to match all the POS tags
        for field in fields:
            field = field.strip('/ ')
            if field in POS_TAGS:
                pos_tags.append(field)
            else:
                break
        # English definition
        self.eng_def = '. '.join(fields[len(pos_tags):])
        # POS tags
        self.pos_tags = map(lambda x: x+'.', pos_tags)

    def to_show(self):
        pos_str = '/'.join(map(lambda x: colored(x, 'green'), self.pos_tags))
        return ' '.join([pos_str, self.eng_def])


class Flashcard(object):

    def __init__(self, word_strs):
        self.word = word_strs[0]
        self.phonogram = word_strs[1]
        # maybe more than one definition
        self.definitions = map(Definition, word_strs[2:])

    def show_base(self):
        print('')
        print(colored(self.word, 'red'))
        print(self.phonogram)

    def show_definition(self):
        for definition in self.definitions:
            print(definition.to_show())

    def show(self):
        self.show_base()
        self.show_definition()

