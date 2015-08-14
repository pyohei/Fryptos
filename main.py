# -*- coding: utf-8 -*-

"""File encrypt.

Put files to public directory by encryption.
And this anchers of relationship.
This module anable change the anchers.
"""
import ConfigParser
import glob
import os
import shutil
import filename
from anchor import Anchor


def main(conf_path='conf/conf.ini'):
    conf = ConfigParser.RawConfigParser()
    conf.read(conf_path)
    anchor = Anchor('text')
    for org_f in __read_files(conf.get('directory', 'file_top')):
        cur_f = anchor.load_cur(org_f)
        enc_f = __make_public_dir(conf.get('directory', 'public_dir',
                                           __encrypt_file(org_f, anchor)))
        __move(org_f, enc_f)
        anchor.change(cur_f, enc_f)
        if os.path.exists(cur_f):
            __delete(cur_f)


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


def __make_public_dir(public_dir, file_path):
    return os.path.join(public_dir, file_path)


def __move(org_f, enc_f):
    os.makedirs(os.path.join(enc_f.split('/')[0:-1]))
    shutil.copy(org_f, enc_f)


def __delete(cur_f):
    shutil.rmtree(cur_f.split('/')[0])
