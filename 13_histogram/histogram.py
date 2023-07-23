'''
An image histogram is a type of histogram that functions as a graphical representation of the tonal distribution in a digital image.
It contains the number of pixels for each tonal value. It allows us to understand the color distribution.
The tonal distribution can be understood by looking at the histogram for a given image
'''

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("red_blue.jpg")
img_vis = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img_vis), plt.title("red_blue RGB")

# look at the size - see how many pixels it has
print(img.shape)

# Histogram
img_hist = cv2.calcHist([img], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
print(img_hist.shape)
plt.figure(), plt.plot(img_hist), plt.title("red_blue RGB Histogram")

# Colorful Histogram
color = ("b", "g", "r")
plt.figure()
for id, c in enumerate(color):
    hist = cv2.calcHist([img], channels=[id], mask=None, histSize=[256], ranges=[0, 256])
    plt.plot(hist, color=c)

# Golden Gate
golden_gate = cv2.imread("goldenGate.jpg")
golden_gate_vis = cv2.cvtColor(golden_gate, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(golden_gate_vis), plt.title("Golden Gate RGB")

# look at the size
print(golden_gate.shape)  # 2448*3264*3

# The size is too big - need to create a mask
mask = np.zeros(golden_gate.shape[:2], np.uint8)  # np.uint8 -> we want zeros int
plt.figure(), plt.imshow(mask, cmap="gray"), plt.title("Mask")
# The mask we created is black so we need to poke a hole in it/apply a filter
mask[1500:2000, 1000:2000] = 255

# Mask the img
masked_img_vis = cv2.bitwise_and(golden_gate_vis, golden_gate_vis, mask=mask)
plt.figure(), plt.imshow(masked_img_vis, cmap="gray"), plt.title("Masked Img")

masked_img = cv2.bitwise_and(golden_gate, golden_gate, mask=mask)
masked_img_hist = cv2.calcHist([golden_gate], channels=[0], mask=mask, histSize=[256], ranges=[0, 256])  #channel[0] = red
plt.figure(), plt.plot(masked_img_hist), plt.title("Masked Golden Gate Hist")

# Histogram equalization / contrast enhancement --> allows us to increase contrast
img = cv2.imread("hist_equ.jpg", 0)
plt.figure(), plt.imshow(img, cmap="gray")

img_hist = cv2.calcHist([img], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
plt.figure(), plt.plot(img_hist)

eq_hist = cv2.equalizeHist(img)
plt.figure(), plt.imshow(eq_hist, cmap="gray")

eq_img_hist = cv2.calcHist([eq_hist], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
plt.figure(), plt.plot(eq_img_hist)


plt.show()























