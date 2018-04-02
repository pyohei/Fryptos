"""Text manager.

Supply text operations.
"""

import csv
import os
import pickle


class Text(object):
    """Text anchor object."""

    def __init__(self):
        self.path = 'anchor.csv'
        self.anchors = {}
        self._load()

    def _load(self):
        """Load anchor line."""
        if not os.path.exists(self.path):
            return
        with open(self.path, 'r') as ff:
            self.anchors = csv.DictReader(ff)
            a = {}
            for n in self.anchors:
                a[n['source']] = n['destination']
        self.anchors = a

    def has(self, org_file):
        return org_file in self.anchors

    def load_cur(self, org_file):
        print self.anchors
        return self.anchors.get(org_file, None)

    def change(self, org_file, enc_file):
        self.anchors[org_file] = enc_file
        try:
            self._save()
            self._load()
        except Exception as e:
            import logging
            logging.critical(e)
            raise SystemError

    def _save(self):
        with open(self.path, 'w') as ff:
            w = csv.DictWriter(ff, fieldnames=['source', 'destination'])
            w.writeheader()
            for k, v in self.anchors.items():
                w.writerow({'source': k, 'destination': v})
