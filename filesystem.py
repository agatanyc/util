"""Functions to work with files and directories."""

import os
import shutil

ls = os.listdir
pwd = os.getcwd
mkdir = os.mkdir

def cp(src, dst):
    if os.path.isdir(src):
        shutil.copytree(src, dst)
    else:
        shutil.copyfile(src, dst)

def rm(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)
