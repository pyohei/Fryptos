"""Anchor object.""" 

class Anchor(object):

    def __init__(self, anc_way, settings={}):
        """Initialize object.

        If you want to extend anchor function,
        you must add new anc_way and new module.
        """
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
