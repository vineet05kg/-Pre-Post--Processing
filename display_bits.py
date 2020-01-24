#!/usr/bin/python

import numpy as np
import cv2
import csv

#initialize list
arr = []

#open csv file
with open(r'C:\Users\Nitharshini\Desktop\work\QR\Toeplitz1.csv') as csvfile: #open csv file
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # read file

    for row in reader:
        if row == [1.0]:  #if value is one
           arr.append(255)#append the array with the value 255
        else:
           arr.append(0) #append array with value 0


arr = np.array(arr,dtype=np.uint8) #convert the list to an array
count = len(arr) #count number of elements in the array
print('count:', count)#print the count
size = np.sqrt(count)#squareroot of the count
print('size:', size)#print the squareroot of the count
#This is a 2x2 array. You can make it 3x3 by adding the number 1,3, or 4. 1 means a grayscale image, 3 means rgb image and 4 means rgb+white image

arr.resize(int(size),int(size)) #resize the array according to integer value of the size



print(arr.shape)# print the shape of the array
print(arr)#print the array

#gray = cv2.cvtColor(arr, cv2.COLOR_BGR2GRAY) # this converts an image from bgr to grayscale
cv2.imwrite('C:/Users/Nitharshini/Desktop/work/QR/image_dis_bits.png',arr) #save the array as image in the path
w = 150 #width
h = 100 #hieght

dim = (w, h) #dimension
resized = cv2.resize(arr, dim, interpolation = cv2.INTER_AREA) #resize the image according to the width and hieght
cv2.imshow('result',arr)# dislay the array in an image
cv2.waitKey(0)# delay the display till close