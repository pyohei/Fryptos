# -*- coding: utf-8 -*-

"""File encrypt.

Put files to public directory by encryption.
And this anchers of relationship.
This module anable change the anchers.
"""
import ConfigParser
import glob
import os
import filename
from anchor import Anchor


def main(conf_path='conf/conf.ini'):
    conf = ConfigParser.RawConfigParser()
    conf.read(conf_path)
    anchor = Anchor('text')
    for org_f in __read_files(conf.get('directory', 'file_top')):
        cur_f = anchor.has(org_f)
        enc_f = __encrypt_file(org_f)
        anchor.change(cur_f, enc_f)


def __read_files(file_path):
    files = glob.glob(file_path)
    for f in files:
        if os.path.isdir(f):
            continue
        yield f


def __encrypt_file(fname, anchor):
    f = filename.change(fname)
    if anchor.haq(f):
        __encrypt_file(filename)
    return f
