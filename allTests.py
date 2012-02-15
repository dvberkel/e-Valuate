#! /usr/bin/env python

import os
from glob import glob

for sourceFile in glob('src/*.py'):
    os.system("python %s" % sourceFile)
