#!/usr/bin/python

import os
import cv2
import argparse
import numpy as np


def get_img_size(path, verbose=True):
    img_size = []
    file_list = os.listdir(path)
    for file in file_list:
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path) and full_path.endswith("JPEG"):
            img = cv2.imread(full_path)
            img_size.append(img.shape)
            if verbose:
                print img.shape
    if verbose:
        avg = np.average(img_size, axis=0)
        print("Average Image Size: {}".format(avg))
    return img_size


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', action='store', help='Search Path')
    args = parser.parse_args()
    get_img_size(args.path)
