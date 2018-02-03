"""File path encryption.

Put files to public directory by encryption.
And this anchers of relationship.
This module anable change the anchers.
"""
import ConfigParser
import glob
import os
import shutil
import filename
from anchor.anchor import Anchor


def main(conf_path='conf/conf.ini', anc_type='text'):
    """Main script of this code."""
    # TODO
    #   Check ini file have correct values.

    # Load configuration.
    conf = ConfigParser.RawConfigParser()
    conf.read(conf_path)
    # Ancker set
    anchor = _load_anchor(conf, anc_type)
    # Read target file
    for org_f in _read_files(conf.get('directory', 'file_top')):
        # Setting path
        cur_f = anchor.load_cur(org_f)
        enc_f = _make_dest_dir(conf.get('directory', 'public_dir'),
                                  _encrypt_file(org_f, anchor))
        # Copy
        _copy(org_f, enc_f)
        # Write change log
        # TODO: need transaction?
        anchor.change(org_f, enc_f)
        # Delete file if exists.
        if cur_f and os.path.exists(cur_f):
            _delete(conf.get('directory', 'public_dir'),
                     cur_f)
    # TODO: Check old file.?


def _load_anchor(config, anc_type):
    """Load anchor object."""
    settings = dict(config.items(anc_type))
    return Anchor(anc_type, settings)


def _read_files(file_path):
    """Read all target files with generator."""
    files = glob.glob(file_path + '/*')
    for f in files:
        if os.path.isdir(f):
            continue
        yield f


def _encrypt_file(fname, anchor):
    """Encrypt file name"""
    f = filename.change(fname)
    if anchor.has(f):
        _encrypt_file(fname)
    return f


def _make_dest_dir(public_dir, file_path):
    """Create destination directory."""
    return os.path.join(public_dir, file_path)


def _copy(org_f, enc_f):
    """Copy source file into destination file."""
    os.makedirs('/'.join(enc_f.split('/')[0:-1]))
    shutil.copy(org_f, enc_f)


def _delete(public_dir, cur_f):
    """Delete encrypt file"""
    delete_path = cur_f.replace(public_dir+'/', '')
    shutil.rmtree(os.path.join(public_dir, delete_path.split('/')[0]))


if __name__ == '__main__':
    main()
