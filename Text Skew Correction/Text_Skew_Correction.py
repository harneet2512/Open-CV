# Import the necessary packages
from typing import List
import numpy as np
import math
import cv2



image = cv2.imread('C:/Users/Harneet singh/Desktop/Open CV/Text Skew Correction/text.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)

cv2.imshow("gray", gray)
cv2.waitKey(0)

thresh = cv2.threshold(gray, 0,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow("thresh", thresh)
cv2.waitKey(0)

coords = np.column_stack(np.where(thresh>0))
angle = cv2.minAreaRect(coords)[-1]
print("Angle: ", angle)

if angle < -45:
	angle = -(90+angle)
else:
	angle = -angle


def rotate_matrix(center: List[int], angle: float, scale: float):
	angle *= math.pi/180
	alpha: float = math.cos(angle)*scale
	beta: float = math.sin(angle)*scale
	M = np.matrix(
		[[alpha, beta, (1-alpha)*center[0] - beta*center[1]],
		[-beta, alpha, beta*center[0] - (1-alpha)*center[1]]])
	return M


(h,w) = image.shape[:2]
center = (w//2, h//2)
M = rotate_matrix(center, angle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h),
	flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
# INTER_CUBIC 

cv2.putText(
	rotated, "Angle: {:.2f} degrees".format(angle),
	(20, h-20), 
	cv2.FONT_HERSHEY_SIMPLEX,
	0.7, (50, 60, 168), 2)
cv2.imshow("Input", image)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)