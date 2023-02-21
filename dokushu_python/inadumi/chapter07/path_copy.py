# -*- coding: utf-8 -*-

import shutil

shutil.copytree('./doc', './data',
                ignore=shutil.ignore_patterns('*.dat', '*.log'))
                