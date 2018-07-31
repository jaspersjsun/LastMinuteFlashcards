#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Description : Flashcard structure
    Author      : FakeCola
    Date        : Jul 25, 2018
"""

from termcolor import colored


# Part-Of-Speech tags
POS_TAGS = [
        'n',
        'adj',
        'adv',
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
        self.pos_tags = list(map(lambda x: x+'.', pos_tags))

    def to_show(self):
        pos_str = '/'.join(map(lambda x: colored(x, 'green'), self.pos_tags))
        return ' '.join([pos_str, self.eng_def])


class Flashcard(object):

    def __init__(self, word_strs):
        self.word = word_strs[0]
        self.phonogram = word_strs[1]
        # maybe more than one definition
        self.definitions = list(map(Definition, word_strs[2:]))

    def show_base(self, screen_show):
        screen_show(colored(self.word, 'red'))
        screen_show(self.phonogram)
        screen_show('')

    def show_definition(self, screen_show):
        for definition in self.definitions:
            screen_show(definition.to_show())

    def show(self, screen_show):
        self.show_base(screen_show)
        self.show_definition(screen_show)
