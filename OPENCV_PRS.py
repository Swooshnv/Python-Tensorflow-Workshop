import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

cap = cv.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    blur = cv.GaussianBlur(frame, (9, 9), 0)
    blur_edge = cv.Canny(blur, 40, 60)
    edge = cv.Canny(frame, 40, 60)
    cv.imshow('Blur', blur)
    cv.imshow('Webcam', frame)
    cv.imshow('Canny', edge)
    cv.imshow('Canny Edge', blur_edge)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
"""
cap = cv.imread('D:/test.jpg', 0)  
width = int(cap.shape[1] * (60/100))
height = int(cap.shape[0] * (60/100))
cap = cv.resize(cap, dsize = (width, height))
blur = cv.GaussianBlur(cap, (7, 7), 1)
denoise= cv.fastNlMeansDenoising(cap, None, h = 21, templateWindowSize  = 6, searchWindowSize = 6)
thresh_denoise = cv.adaptiveThreshold(denoise, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 13, 25)
cv.imshow('text', cap)
#cv.imshow('blur', blur)
cv.imshow('denoise', denoise)
cv.imshow('thresh_denoise', thresh_denoise)
cv.waitKey(0)
"""
cap.release()
cv.destroyAllWindows()