# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 18:01:54 2020

@author: Harneet singh
"""

import numpy as np
import imutils
import cv2



# LOAD THE IMAGE FROM DISK
image = cv2.imread('C:/Users/Harneet singh/Desktop/New folder/Q3/Image for Q3.jpg')

# LOOP OVER THE ROTATION ANGLES
for angle in np.arange(0,360,15):
	rotated = imutils.rotate(image, angle)
	cv2.imshow('Rotated (problematic)', rotated)
	cv2.waitKey(0)

# LOOP OVER THE ROTATION ANGLES AGAIN, THIS TIME ENSURING
# NO PART OF THE IMAGE IS CUT OFF
for angle in np.arange(0,360,15):
	rotated = imutils.rotate_bound(image, angle)
	cv2.imshow('Rotated (problematic)', rotated)
	cv2.waitKey(0)