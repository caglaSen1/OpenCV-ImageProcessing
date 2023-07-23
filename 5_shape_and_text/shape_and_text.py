import cv2
import numpy as np

# Create black img
# If the amplitude of the pixel is 0 we see black, if 1 we see white
# Each pixel of the image created with the np.zeros() function has a value of 0.
img_black = np.zeros((512, 512, 3), np.uint8)
print(img_black.shape)
cv2.imshow("Black", img_black)

# Each pixel of the image created with the np.ones() function has a value of 1.
# However, with the expression * 255, each pixel value is multiplied by 255 (white) and the image is converted to white.
img_white = np.ones((512, 512, 3), np.uint8) * 255
print(img_white.shape)
cv2.imshow("White", img_white)

# Draw Line
cv2.line(img_black, (0, 0), (512, 512), (0, 255, 0), 3)
# line(img, start point, end point, color(openCV accepts RGB as BRG), thickness)
cv2.imshow("Line", img_black)

# Draw Rectangle
cv2.rectangle(img_black, (0, 0), (256, 256), (255, 0, 0), cv2.FILLED)
# rectangle(img, start point, end point, color, thickness/filled)
cv2.imshow("Rectangle", img_black)

# Draw Circle
cv2.circle(img_black, (300, 300), 45, (0, 0, 255), cv2.FILLED)
# circle(img, center, radius, color, thickness/filled)
cv2.imshow("Circle", img_black)

# Text
cv2.putText(img_black, "Img", (350, 350), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
# putText(img, text, start point, font, thickness, color)
cv2.imshow("Text", img_black)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
