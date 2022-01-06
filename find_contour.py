# load image, change color spaces, and smoothing
import cv2
import numpy as np
from IPython import display
from matplotlib import pyplot as plt


img = cv2.imread("../images/bear_renamed/bear_003.png")

# Convert to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert to binary
ret, bin_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)

# Check
cv2.imshow("gray", bin_img)
cv2.waitKey(0)

# Extract contours
contours, hierarchy = cv2.findContours(
    bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

# Remove small contours
contours = list(filter(lambda x: cv2.contourArea(x) > 100, contours))

# Draw contours
cv2.drawContours(img, contours, -1, color=(0, 0, 255), thickness=2)

cv2.imshow("color", img)
cv2.waitKey(0)

