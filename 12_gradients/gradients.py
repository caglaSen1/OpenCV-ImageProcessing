'''
An image gradient is a directional change in intensity or color in an image.
Used in edge detection.
'''

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("sudoku.jpg", 0)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off"), plt.title("Original img")

# x gradient (find the gradient on the x-axis / detection of vertical edges)
sobel_x = cv2.Sobel(img, ddepth=cv2.CV_16S, dx=1, dy=0, ksize=5)   # ddepth - depth of the output
plt.figure(), plt.imshow(sobel_x, cmap="gray"), plt.axis("off"), plt.title("Sobel X")

# y gradient (find the gradient on the y-axis / detection of horizontal edges)
sobel_y = cv2.Sobel(img, ddepth=cv2.CV_16S, dx=0, dy=1, ksize=5)
plt.figure(), plt.imshow(sobel_y, cmap="gray"), plt.axis("off"), plt.title("Sobel y")

# Laplacian Gradian - For detection of both horizontal and vertical edges
laplacian = cv2.Laplacian(img, ddepth=cv2.CV_16S)
plt.figure(), plt.imshow(laplacian, cmap="gray"), plt.axis("off"), plt.title("Laplacian")

plt.show()
