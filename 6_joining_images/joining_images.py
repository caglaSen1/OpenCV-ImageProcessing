import cv2
import numpy as np

img_name = "lenna.png"

img = cv2.imread(img_name)
cv2.imshow("Original", img)

# Horizontal join
horizontal = np.hstack((img, img))
cv2.imshow("Horizontal", horizontal)

# Vertical join
vertical = np.vstack((img, img))
cv2.imshow("Vertical", vertical)

cv2.waitKey(0) & 0xFF == 27
