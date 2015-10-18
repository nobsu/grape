#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
root = os.path.dirname(__file__)
#sys.path.insert(0, os.path.join(root, 'ext-libs'))
sys.path.insert(0, root)

from grape.web import create_app
application = create_app()

if __name__ == '__main__':
    application.run()
