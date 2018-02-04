"""Text manager.

Supply text operations.
"""

import csv
import os
import pickle


class Text(object):

    def __init__(self, settings):
        self.file_path = settings.get('ancfile_path', 'anc.txt')
        # New saving file(tsv).
        self.path = settings.get('ancfile_path', 'anc.tsv')
        print self.path
        self.anchors = {}
        # New anchor
        self.new_anchors = {}
        self._load()
        self.encrypted_words = []
        self._load_encrypt_words()

    def _load(self):
        if not os.path.exists(self.file_path):
            return
        with open(self.file_path, 'r') as f:
            self.anchors = pickle.load(f)
        with open(self.path + '.tsv', 'r') as ff:
            self.new_anchors = csv.DictReader(ff)
            a = {}
            for n in self.new_anchors:
                a[n['source']] = n['destination']
        print "]]]]"
        print self.anchors == a
        print "]]]]"

    def _load_encrypt_words(self):
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
            self._save()
            self._load()
        except Exception as e:
            print e
            raise

    def _save(self):
        tmp_file = self.file_path + '.org'
        with open(tmp_file, 'w') as f:
            pickle.dump(self.anchors, f)
        with open(self.path + '.tsv', 'w') as ff:
            w = csv.DictWriter(ff, fieldnames=['source', 'destination'])
            w.writeheader()
            for k, v in self.anchors.items():
                w.writerow({'source': k, 'destination': v})

        self.__change_file(tmp_file)

    def __change_file(self, tmp_file):
        bk_file = self.file_path + '.bk'
        if os.path.exists(self.file_path):
            os.rename(self.file_path, bk_file)
        os.rename(tmp_file, self.file_path)
