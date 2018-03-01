"""File path encryption.

Put files to public directory by encryption.
And this anchers of relationship.
This module anable change the anchers.
"""
import glob
import os
import shutil
import filename
from anchor.anchor import Anchor


def main(src, target, f):
    """Main script of this code."""
    # TODO
    #   Check ini file have correct values.

    # Ancker set
    anchor = Anchor('text')
    # Read target file
    for org_f in _read_files(src):
        # Setting path
        cur_f = anchor.load_cur(org_f)
        enc_f = _make_dest_dir(target, _encrypt_file(org_f, anchor))
        # Copy
        _copy(org_f, enc_f)
        # Write change log
        # TODO: need transaction?
        anchor.change(org_f, enc_f)
        # Delete file if exists.
        if cur_f and os.path.exists(cur_f):
            _delete(target, cur_f)
    # TODO: Check old file.?


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
    # TODO: add usage
    import argparse
    from os.path import expanduser
    home_dir = expanduser('~')
    p = argparse.ArgumentParser(description='Encrypt your files.')
    p.add_argument('source')
    p.add_argument('target')
    p.add_argument('-f', '--file', default=home_dir, type=str)
    p.print_usage()

    args = p.parse_args()
    src = str(args.source)
    tgt = str(args.target)
    f = str(args.file)
    
    print(src, tgt, f)
    main(src, tgt, f)
