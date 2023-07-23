import cv2

# Read and show normal img
img = cv2.imread("lenna.png")
cv2.imshow("Original", img)

# Shape of normal img
height, width, channels = img.shape  # If img is RGB/BGR
# height, width = img.shape  # If img is gray scale
print(f"Img shape: {height}, {width}, {channels}")

# Resize img
img_resized = cv2.resize(img, (800, 800))
cv2.imshow("Img Resized", img_resized)
print("Resized img shape: ", img_resized.shape)

# Crop img
img_cropped = img[100:400, :300]  # from 100th to 400th pixels on the x-axis(height) and from 0 to 300th pixels on the y-axis(width)
# Important: Normally it can be thought as [width, height] but in opencv it is [height, width]
"""
points (Column, Row) (X, Y)
0/0 -----X----->
 |
 |
 Y
 |
 |
 v
"""
cv2.imshow("Img Cropped", img_cropped)
print("Cropped img shape: ", img_cropped.shape)

key = cv2.waitKey(0) & 0xFF  # press any key on the keyboard and the windows close
cv2.destroyAllWindows()


