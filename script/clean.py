#!/usr/bin/env python

import os
import sys

from lib.util import rm_rf


SOURCE_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def main():
  os.chdir(SOURCE_ROOT)
  try:
    rm_rf('node_modules')
    rm_rf('dist')
    rm_rf('out')
    rm_rf('spec/node_modules')
    rm_rf('vendor/brightray/vendor/download/libchromiumcontent')
  except WindowsError:  # pylint: disable=E0602
    pass


if __name__ == '__main__':
  sys.exit(main())
