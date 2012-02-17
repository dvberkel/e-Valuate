#! /usr/bin/env python

import os
from glob import glob

for sourceFile in glob('evaluate/*.py'):
    os.system("python %s" % sourceFile)
