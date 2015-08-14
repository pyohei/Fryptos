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
        enc_f = __make_public_dir(conf.get('directory', 'public_dir'),
                                  __encrypt_file(org_f, anchor))
        __move(org_f, enc_f)
        anchor.change(org_f, enc_f)
        if cur_f and os.path.exists(cur_f):
            __delete(conf.get('directory', 'public_dir'),
                     cur_f)


def __read_files(file_path):
    files = glob.glob(file_path + '/*')
    for f in files:
        if os.path.isdir(f):
            continue
        yield f


def __encrypt_file(fname, anchor):
    f = filename.change(fname)
    if anchor.has(f):
        __encrypt_file(fname)
    return f


def __make_public_dir(public_dir, file_path):
    return os.path.join(public_dir, file_path)


def __extract_public_dir(public_dir, file_path):
    return file_path.lstrip(public_dir)


def __move(org_f, enc_f):
    os.makedirs('/'.join(enc_f.split('/')[0:-1]))
    shutil.copy(org_f, enc_f)


def __delete(public_dir, cur_f):
    delete_path = cur_f.replace(public_dir+'/', '')
    shutil.rmtree(os.path.join(public_dir, delete_path.split('/')[0]))


if __name__ == '__main__':
    main()
