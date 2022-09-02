#Assignment 0, Quesiton 2

import cv2
import numpy as np


img = cv2.imread('input.png')
cv2.imshow("original", img)

height = img.shape[0]
width = img.shape[1]

array1 = np.array((255, 0, 0))
array2 = np.array((0, 255, 0))
array3 = np.array((0, 0, 255))

for y in range(0, height):
    for x in range (0, width):
        distX = np.linalg.norm(img[y, x] - array1)
        distY = np.linalg.norm(img[y, x] - array2)
        distZ = np.linalg.norm(img[y, x] - array3)

        if (distX > distY and distX > distZ):
            img[y, x] = distX

        if (distY > distZ):
            img[y, x] = distY

        else:   img[y, x] = distZ

cv2.imwrite('output1.png', img)
