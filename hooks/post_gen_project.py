#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import shutil

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('post_gen_project')

ALL_TEMP_FOLDERS = ['_docs', '_licenses']

def remove_temp_folders(temp_folders):
    """https://github.com/pytest-dev/cookiecutter-pytest-plugin/blob/master/hooks/post_gen_project.py#L42"""
    for folder in temp_folders:
        logger.info('Remove temporary folder: %s', folder)
        shutil.rmtree(folder)

if __name__ == '__main__':
    remove_temp_folders(ALL_TEMP_FOLDERS)
