from gettext import npgettext
import cv2
import numpy as np

img = cv2.imread('my_wall.jpeg',cv2.IMREAD_GRAYSCALE)

thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY)[1]

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
morph = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel)

letter = morph.copy()
cntrs = cv2.findContours(morph, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cntrs = cntrs[0] if len(cntrs) == 2 else cntrs[1]
for c in cntrs:
    area = cv2.contourArea(c)
    if area < 100:
        cv2.drawContours(letter,[c],0,(0,0,0),-1)

edges = cv2.Canny(letter,200,200)

cv2.imshow('K_thresh',thresh)
cv2.imshow('K_morph',morph)
cv2.imshow('K_letter',letter)
cv2.waitKey(0)