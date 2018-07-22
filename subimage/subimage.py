#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
import os
import sys

logger = logging.getLogger(__file__)
formatter = logging.Formatter('[%(levelname)s] %(message)s')
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def main():
    parser = argparse.ArgumentParser(
        description='Check if an image is a subimage of another one',
    )
    parser.add_argument(
        'file1',
        help='path to first image',
        metavar='FIRST_IMAGE_PATH',
        type=lambda x: is_valid_file(parser, x),
    )
    parser.add_argument(
        'file2',
        help='path to second image',
        metavar='SECOND_IMAGE_PATH',
        type=lambda x: is_valid_file(parser, x),
    )
    args = parser.parse_args()
    file1 = args.file1
    file2 = args.file2

    logger.info(
        'Checking subimage between {file1} and {file2}'.format(
            file1=file1,
            file2=file2,
        )
    )
    raise NotImplementedError(
        'Do NOT use this script. Development in progress',
    )


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error('The file %s does not exist!' % arg)
    else:
        return arg


if __name__ == '__main__':
    main()
