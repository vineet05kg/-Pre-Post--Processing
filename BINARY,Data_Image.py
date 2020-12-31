##############################################################################################################
#                           IMAGE PLOTTING OF THE BINARY DATA TAKEN FROM CSV FILE                            #
##############################################################################################################

# To call the different related libraries required for the program//

import numpy as np
import cv2
import csv
##############################################################################################################

List_x = []  # To initialise the list//

with open(r'D:/Python/VacuumData_Analysis/ForAcquired_Date[18.Dec.2019]viaAPD/2.5MSas/Toeplitz1_1.csv') as csvfile:
    # To locate the binary data file//
    fileread = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # To read the binary data file//
    
##############################################################################################################

    for row in fileread:
        if row == [1.0]:  # To find the value in row as one//
           List_x.append(255)  # To append the one value's of row with the significant value 255 //
        else:  # To find the value in row as zero//
           List_x.append(0)  # To append the zero value's of row with the significant value 0//

Array_y = np.array(List_x, dtype = np.uint8)  # To convert the list in to the array//
Element_count = len(Array_y)  # To count the number of elements in array//
print('Total number of count in the array = ', Element_count)
A = np.sqrt(Element_count)  # To find the square root of the total length of the Array_y to determine the corresponding
# size of each dimension of the same resized Arrar_y//

Array_y.resize(int(A),int(A))  # To determine the '2 x 2' Array, i.e. of two dimensions. By the command of
# Array_y.resize(int(A),int(A),1) it is same as of Array_y.resize(int(A),int(A)) means a 'grayscale binary
# data image'. By the command of Array_y.resize(int(A),int(A),3) it shows 'binary rgb image' of spatial
# dimension one-third of the grayscale binary data image. Whereas the command of Array_y(int(A), int(A), 4)
# shows 'binary rgb+white image' of spatial dimension one-fourth//

print(Array_y.shape)  # To print the shape of the array//
print(Array_y)  # To print the array//
##############################################################################################################
# To save the binary data image to the desired location//

cv2.imwrite('D:/Python/VacuumData_Analysis/ForAcquired_Date[18.Dec.2019]viaAPD/2.5MSas/BinaryData_'
            'Image.png',Array_y)  # To save the array image //
cv2.imshow('BinaryData_Image',Array_y)  # To display the binary data image//
cv2.waitKey(0)  # To delay the image till close//

'''

        For reference related to this program check the mentioned URL attached herein below
        https://www.educative.io/edpresso/how-to-convert-a-list-to-an-array-in-python
        https://docs.python.org/3/library/statistics.html
        https://techtutorialsx.com/2018/06/24/python-opencv-saving-an-image-to-the-file-system/
        https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html
        https://www.geeksforgeeks.org/python-opencv-cv2-imread-method/        

'''
