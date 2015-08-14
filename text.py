# -*- coding: utf-8 -*-

"""Text manager.

Supply text operations.
"""

import os
import pickle


class Text(object):

    def __init__(self, file_path='anc.txt'):
        self.file_path = file_path
        self.anchors = self.__load()

    def __load(self):
        with open(self.file_path, 'r') as f:
            self.anchors = pickle.load(f)

    def has(self, org_file):
        return org_file in self.anchors

    def load_cur(self, org_file):
        return self.anchors.get(org_file, None)

    def change(self, org_file, enc_file):
        self.anchors[org_file] = enc_file
        try:
            self.__save()
            self.__load()
        except Exception as e:
            print e
            return

    def __save(self):
        tmp_file = self.file_path + '.org'
        with open(tmp_file, 'w') as f:
            pickle.dump(f, self.anchors)
        self.__change_file(tmp_file)

    def __change_file(self, tmp_file):
        bk_file = self.file_path + '.bk'
        os.rename(self.file_path, bk_file)
        os.rename(tmp_file, self.file_path)
