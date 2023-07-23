import cv2
import numpy as np

img_name = "cart.png"
img = cv2.imread(img_name)
cv2.imshow("Original", img)

width = 400
height = 500

# we opened the image in paint and saw the positions of the corner pixels:
# pts1 --> the corners of the picture we want to turn
pts1 = np.float32([[203, 1], [1, 472], [540, 150], [338, 617]])
# pts1 = np.float32([[left top], [left bottom], [right top], [right bottom]])

# pts2 --> the corners of the picture I want to get
pts2 = np.float32([[0, 0], [0, height], [width, 0], [width, height]])

# The transform matrix that must be applied to move from point 1 to point 2
matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)

# performs the warping operation: cv2.warpPerspective(image to be warped, transformation matrix, dimensions of the final image)
img_transformed = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Transformed Image", img_transformed)

cv2.waitKey(0) & 0xFF
