# -*- coding: utf-8 -*-

"""Anchor of file.

"""


class Anchor(object):

    def __init__(self, anc_way, settings={}):
        if anc_way == 'text':
            from text import Text as Record
        self.anchor = Record(settings)

    def has(self, filename):
        """Check encrypt file name."""
        return self.anchor.has(filename)

    def load_cur(self, filename):
        """Load current encrypted filename"""
        return self.anchor.load_cur(filename)

    def change(self, org, dst):
        """Change anchor"""
        self.anchor.change(org, dst)
