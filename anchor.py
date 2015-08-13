# -*- coding: utf-8 -*-

"""Anchor of file.

"""


class Anchor(object):

    def __init__(self, anc_way):
        pass

    def has(self, filename):
        """Check encrypt file name."""
        pass

    def load_cur(self, filename):
        """Load current encrypted filename"""
        pass

    def put(self, org_filename, enc_filename):
        """Put filename into anchor"""
        pass

    def change(self, org, dst):
        """Change anchor"""
        pass
