# -*- coding: utf-8 -*-

"""Text manager.

Supply text operations.
"""

import os
import pickle


class Text(object):

    def __init__(self, file_path='anc.txt'):
        self.file_path = file_path
        self.anchors = {}
        self.__load()
        self.encrypted_words = []
        self.__load_encrypt_words()

    def __load(self):
        if not os.path.exists(self.file_path):
            return
        with open(self.file_path, 'r') as f:
            self.anchors = pickle.load(f)

    def __load_encrypt_words(self):
        words = []
        for w in self.anchors.values():
            words += w.split('/')
        self.encrypted_words = words

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
            raise

    def __save(self):
        tmp_file = self.file_path + '.org'
        with open(tmp_file, 'w') as f:
            pickle.dump(self.anchors, f)
        self.__change_file(tmp_file)

    def __change_file(self, tmp_file):
        bk_file = self.file_path + '.bk'
        if os.path.exists(self.file_path):
            os.rename(self.file_path, bk_file)
        os.rename(tmp_file, self.file_path)
