import cv2

# Normal Image Name
img_name = "messi.jpg"

# Read Normal Image
img_normal = cv2.imread(img_name)

# Show Normal Image
cv2.imshow("Normal Image", img_normal)

# Read As Gray Scale
img_gray = cv2.imread(img_name, 0)  # 0 allows to import as gray scale

# Show Gray Scale Image
cv2.imshow("Gray Image", img_gray)

# Connecting keyboard
key = cv2.waitKey(0) & 0xFF
if key == 27:  # (27 == esc)
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite("messi_gray.png", img_gray)  # Saving normal image in gray scale
    cv2.destroyAllWindows()
