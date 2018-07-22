#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python imports
import argparse
import logging
import os
import sys

# 3rd party imports
import cv2
import numpy as np
import scipy.ndimage as sp


logger = logging.getLogger(__file__)
formatter = logging.Formatter('[%(levelname)s] %(message)s')
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def main():
    parser = argparse.ArgumentParser(
        description=(
            'Check if an image is a subimage of another one. '
            # TODO cleanup
            'This script is still in progress, '
            'proper error handling is not setup yet.'
        ),
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
    file1_path = args.file1
    file2_path = args.file2

    logger.info(
        'Checking subimage between {file1} and {file2}'.format(
            file1=file1_path,
            file2=file2_path,
        )
    )
    subimage_checker = SubimageChecker(file1_path, file2_path)
    coordinates = subimage_checker.check()
    if coordinates is None:
        logger.info("No subimage found")
    else:
        logger.info("Subimage found at ({x}, {y})".format(
            x=coordinates[0],
            y=coordinates[1],
        ))


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
    def __init__(self, file1_path, file2_path):
        self.image1 = cv2.imread(file1_path, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        self.image2 = cv2.imread(file2_path, cv2.CV_LOAD_IMAGE_GRAYSCALE)

        self.image1_canny = cv2.Canny(self.image1, 32, 128, apertureSize=3)
        self.image2_canny = cv2.Canny(self.image2, 32, 128, apertureSize=3)

    def validate_images(self):
        """
        Various checks on the images
        """
        if not self._validate_are_images():
            return False

        if not self._validate_image_dimensions():
            return False

        return True

    def _validate_are_images(self):
        if self.image1 is None:
            logger.warning(
                'Path to first file is not pointing '
                'to an image.'
            )
            return False

        if self.image2 is None:
            logger.warning(
                'Path to second file is not pointing '
                'to an image.'
            )
            return False

        return True

    def _validate_image_dimensions(self):
        """
        Checking that an image can be subimage of another one,
        based on dimensions
        eg. (100x200) and (50x300) can't be subimages
        """
        # getting the first two,
        # in case image is a binary and is missing `channels`
        height1, width1 = self.image1.shape[:2]
        height2, width2 = self.image2.shape[:2]
        sizes_diff = [height1 - height2, width1 - width2]
        if sum([1 for item in sizes_diff if item > 0]) == 1:
            logger.warning('Images are incompatible sizes')
            return False

        return True

    def check(self):
        """
        perform the actual subimage check
        """
        if not self.validate_images():
            return None

        result = cv2.matchTemplate(
            self.image1_canny,
            self.image2_canny,
            cv2.TM_CCOEFF_NORMED,
        )
        (y, x) = np.unravel_index(result.argmax(), result.shape)

        confidence = 0.8
        result[result >= confidence] = 1.0
        result[result < confidence] = 0.0

        connected_components = self.get_connected_components(result)

        if not connected_components:
            return None

        return [x, y]

    def get_connected_components(self, image):
        """
        Finds connected image components in a matchTemplate result and
        returns their coordinates.
        """
        labels, _ = sp.measurements.label(image)
        objects = sp.measurements.find_objects(labels)
        return objects


if __name__ == '__main__':
    main()
