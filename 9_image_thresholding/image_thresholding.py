import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(img, cmap="gray")  # cmap = "gray" --> shows img gray in figure
plt.axis("off")  # we closed the axes in the figure
plt.show()

# 0 black, 255 white - so low scales are dark color, high scales are light color

# Threshold - this method returns two things, one is not important for us
# type=cv2.THRESH_BINARY --> make the values between 60-255 white (will make 255) and others black (will make 0)
_, thresh_img = cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY)

plt.figure()
plt.imshow(thresh_img, cmap="gray")
plt.axis("off")
plt.show()

# type=cv2.THRESH_BINARY_INV --> make the values between 60-255 black (will make 0) and others white (will make 255)
_, thresh_img = cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY_INV)
plt.figure()
plt.imshow(thresh_img, cmap="gray")
plt.axis("off")
plt.show()


# Adaptive threshold
'''
Sometimes we need to use adaptive threshold 
(Adaptive threshold is calculated separately for neighboring pixels)
There are shadows in some parts of the picture. For example, part of the mountain is light while part of it is dark because it is in shadow.
When we apply threshold, it only affects a part of the mountain because of the shadows. 
But we want the mountain to disappear/not disappear as a whole.
For this we use adaptive thresholding. 
In adaptive thresholding, the algorithm calculates the threshold for a small region of the image, 
so we get different thresholds for different regions of the same image. 
'''

thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
# adaptiveThreshold(img, max value, the method to be used for the equalization algorithm is averaged according to the constant c,
# cv2.THRESH_BINARY/cv2.THRESH_BINARY_INV (white/black), 11 = block size,
# 8 = c constant, i.e. the value to be subtracted from the weighted average)
plt.figure()
plt.imshow(thresh_img2, cmap="gray")
plt.axis("off")
plt.show()


