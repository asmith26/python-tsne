#!/usr/bin/python

from skimage.io import imread
import glob
import os
import json
import sys

label = sys.argv[1] # e.g. c0, c1, ...
src_dir = "/home/andyandy/data/kaggle/state-farm/train/{}".format(label)
#src_dir = "/home/andyandy/Desktop/state-farm/imgs/train/{}".format(label)

RGB = False

#i=0
if RGB:
# JUST REMOVE flatten=Trure from `img = imread( ...`
    sys.exit("ERROR: You should not have ended here.")
else:
    for jpg_file in glob.iglob( os.path.join( src_dir, "*.jpg" ) ):
        img = imread( jpg_file, flatten=True )
        img_pixels = []
#For testing: only run first few instances
#        if i >= 2:
#            continue
        for j in xrange( len(img) ):
            for k in xrange( len(img[j]) ):
#                print img[j][k]
                img_pixels.append( float(img[j][k]) )

        print img_pixels
#        i += 1
