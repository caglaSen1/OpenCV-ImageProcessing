'''
Blur is useful for removing noise. Details are reduced. Eliminates high frequency content (noise, edges, etc.).
OpenCv provides three main types of blurring techniques: Mean blur, Gaussian blur, Median blur

Mean blur:
This is done by wrapping the image with a normalized box filter. For example, a 5x5 box slides over the image
and averages the pixels it lands on and writes this average to the center/replaces it with the central element.
Since the other pixels will dominate the noisy pixel, the noise is eliminated. In other words, blurring occurs because
the amplitude of the central element is changed.

Gaussian blurring:
Gaussian kernel is used instead of the box filter used in mean blur. Instead of taking the average
values, the Gaussian kernel performs operations according to the values we specify.

# Median blur:
The kernel takes the median of all pixels under its area and replaces the central element with this median value.
'''

import cv2
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# Opening img
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("Original")


# Mean Blur:
mean_blur = cv2.blur(img, ksize=(3, 3))  # ksize = kernel size
plt.figure(), plt.imshow(mean_blur), plt.axis("off"), plt.title("Mean Blur")


# Gaussian Blur:
gaussian_blur = cv2.GaussianBlur(img, ksize=(3, 3), sigmaX=7)  # # If we do not write sigmaY, it is automatically equal to sigmaX
plt.figure(), plt.imshow(gaussian_blur), plt.axis("off"), plt.title("Gauss Blur")


# Medyan Blur
median_blur = cv2.medianBlur(img, ksize = 3)
plt.figure(), plt.imshow(median_blur), plt.axis("off"), plt.title("Median Blur")


# Create noise functions to see what happens when we use blurring techniques:
def gaussian_noise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5

    # We obtained gaussian noise with a certain mean and standard deviation:
    gauss = np.random.normal(mean, sigma, (row, col, ch))

    gauss = gauss.reshape(row, col, ch)  # we are once again assured of its size

    # To get the noisy image, we add the noise to the original image
    noisy = image + gauss

    return noisy


def salt_pepper_noise(image):
    row, col, ch = image.shape
    salt_and_pepper_ratio = 0.8   # salt pepper ratio
    amount = 0.004

    noisy = np.copy(image)   # copy of original img

    # Salt - white
    # Determine the number of whites:
    num_salt = np.ceil(amount * image.size * salt_and_pepper_ratio)  # ceil rounds a decimal number to an integer
    # Randomize the coordinates:
    coords = [np.random.randint(0, i-1, int(num_salt)) for i in image.shape]  # np.random.randint(low, high, size)
    # In the random coordinates we created, we add the whites to the image:
    noisy[coords] = 1   # 1 = white

    # Pepper - black
    num_pepper = np.ceil(amount * image.size * (1 - salt_and_pepper_ratio))
    coords = [np.random.randint(0, i-1, int(num_pepper)) for i in image.shape]
    noisy[coords] = 0

    return noisy


# IMPORTANT: Normally the values in our original image are between 0-255, we need to normalize these values, that is,
# move them between 0-1. Because the noise we created is a noise with a mean of 0, if we add this noise to the image
# with an amplitude value of 0-255, nothing will appear, so we need to normalize.
# Import and NORMALIZE
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255  # normalize (move the values ranging between 0-255 between 0-1)
plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("original normalized")

# Create gauss noisy img
gaussian_noisy_image = gaussian_noise(img)
plt.figure(), plt.imshow(gaussian_noisy_image), plt.axis("off"), plt.title("Image Gaussian Noisy")

# Gauss blur - reduce the noise we create
gb2 = cv2.GaussianBlur(gaussian_noisy_image, ksize=(3, 3), sigmaX=7)
plt.figure(), plt.imshow(gb2), plt.axis("off"), plt.title("Image Gaussian Noisy with Gauss Blur")


# Create salt and pepper noisy img
salt_pepper_image = salt_pepper_noise(img)
plt.figure(), plt.imshow(salt_pepper_image), plt.axis("off"), plt.title("SP Image")

# Median blur - reduce the noise we create
mb2 = cv2.medianBlur(salt_pepper_image.astype(np.float32), ksize=3)
plt.figure(), plt.imshow(mb2), plt.axis("off"), plt.title("SP Image with Median Blur")

plt.show()
cv2.waitKey(0) & 0xFF



