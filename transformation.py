import numpy as np
import cv2 as cv

img = cv.imread('photos/cats 2.jpg')

cv.imshow("Boston", img)

def translate(img, x,y):
    transMat = np.float64([[1,0,x],[0,1,y]])
    dimesions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMat,dimesions)

# -x --> left
# -y --> Up
# x -- Right
# y --> Down

translated = translate(img, -100, 100)
cv.imshow('Translated',translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width)= img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle,1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Roatated',rotated)

# Resizing
resized = cv.resize(img, (500,500),interpolation=cv.INTER_LINEAR)
cv.imshow('Resized', resized)

#Flipping
flip = cv.flip(img, -1) # -1 for vertical flip and 1 for horizontal flip
cv.imshow('Flip',flip)

# Croping 
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey()