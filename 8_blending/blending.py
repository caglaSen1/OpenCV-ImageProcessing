import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("img1.jpg")
# When uploading images to openCv, they are uploaded in BGR color scale by default.
# If we want to see clear picture in matplotlib we should convert it to RGB format
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

img2 = cv2.imread("img2.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# When plt.figure() is called, a new empty figure is created, allowing you to work on it.
# After creating a figure, you can add images to it using the plt.imshow() function.
plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# Two matrices of different sizes cannot be summed so the size of the images must be the same
print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1, (600, 600))
img2 = cv2.resize(img2, (600, 600))

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# Blended img = alpha*img1 + beta*img2
img_blended = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.5, gamma=0)
plt.figure()
plt.imshow(img_blended)

plt.show()
cv2.waitKey(0) & 0xFF
