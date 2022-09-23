"""
Python program that will convert an image to a pencil drawing!!!

I will need to import the cv2 library since it is not installed, I used
    the following on a cmd promt to easily install:
    
    python3 -m pip install opencv-python
    python3 -m pip install Pillow

Now to import the library I just installed:
Also importing another library named Pillow to rezize the image:
"""
import cv2
from PIL import Image

#   First to tell the program "where" and "what" to look for, with:
img_location = 'C:\\Users\\mjame\\OneDrive\GitHub\\marduk_james\\python_stuff\\image_to_text\\'
filename = 'baby_n_me.jpg'

#   Now we have to read the image:
img = cv2.imread(img_location + filename)

#   Converting to grayscale:
gray_image  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#   Invert image:
inverted_grey_image = 255 - gray_image

#   Blurring the image by gaussian function:
blurred_image = cv2.GaussianBlur(inverted_grey_image, (21,21), 0)

#   Invert the blurred image:
inverted_blurred_image = 255 - blurred_image

#   Create the pencil sketch image:
pencil_sketch_IMG = cv2.divide(gray_image, inverted_blurred_image, scale = 256.0)


#   Lets check to see that the file is working by viewing it:
cv2.imshow('Original Image', img)
cv2.imshow('New Image', pencil_sketch_IMG)
cv2.imwrite('New.jpg', pencil_sketch_IMG)
cv2.waitKey(0)





















