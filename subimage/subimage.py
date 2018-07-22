#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python imports
import argparse
import logging
import os
import sys

# 3rd party imports
import cv2
import numpy


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
    file_path1 = args.file1
    file_path2 = args.file2

    logger.info(
        'Checking subimage between {file1} and {file2}'.format(
            file1=file_path1,
            file2=file_path2,
        )
    )
    subimage_checker = SubimageChecker(file_path1, file_path2)
    subimage_checker.check()


def is_valid_file(parser, arg):
    """
    Checks if a file exists on disk at the `arg` path
    """
    if not os.path.exists(arg):
        parser.error('The file %s does not exist!' % arg)
    else:
        return arg


class SubimageChecker(object):
    """
    Helper class to check if an image is cropped from another one
    """
    def __init__(self, file_path1, file_path2):
        self.image1 = cv2.imread(file_path1)
        self.image2 = cv2.imread(file_path2)

    def check(self):
        result = cv2.matchTemplate(
            self.image1,
            self.image2,
            cv2.TM_CCOEFF_NORMED,
        )
        print numpy.unravel_index(result.argmax(), result.shape)


if __name__ == '__main__':
    main()
