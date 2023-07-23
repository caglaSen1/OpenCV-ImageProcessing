'''
Erode: Erodes the boundaries of the foreground object.

Dilate: The opposite of erosion, it increases the white area in the image.

Opening: Erode + Dilate --> useful for removing noise. With erode the white in the image is reduced,
with dilate the white text is enlarged and the image is restored to its original state by removing noise.

Closing: The opposite of opening. Dilate + Erode --> is used to close small black dots on the foreground object.

Morphological Gradient: It is the difference between dilate and erode.(Dilate - Erode)
An image is expanded and eroded and the difference between them is taken. Example: White framed text with a black center.
'''

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("datai_team.jpg", 0)  # 0 to import the image in gray scale and reduce it to two sizes
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off"), plt.title("Original Img")
print(img.shape)

kernel = np.ones((5, 5), dtype=np.uint8)

# Erode
result = cv2.erode(img, kernel, iterations=1)
plt.figure(), plt.imshow(result, cmap="gray"), plt.axis("off"), plt.title("Erode Img")


# Dilate
result = cv2.dilate(img, kernel, iterations=1)
plt.figure(), plt.imshow(result, cmap="gray"), plt.axis("off"), plt.title("Dilated Img")


# Opening - create white noise
white_noise = np.random.randint(0, 2, size=img.shape[:2])  # normalize noise
white_noise = white_noise * 255  # Multiply the normalized noise we obtained by 255 to the 0-255 scale
plt.figure(), plt.imshow(white_noise, cmap="gray"), plt.axis("off"), plt.title("White Noise")

# Opening - add noise created to the img
noise_img = white_noise + img
plt.figure(), plt.imshow(noise_img, cmap="gray"), plt.axis("off"), plt.title("Img with White Noice")

# Opening - Remove the noise in the picture with the opening method
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure(), plt.imshow(opening, cmap="gray"), plt.axis("off"), plt.title("Opening")


# Closing - create black noise
black_noise = np.random.randint(0, 2, size=img.shape[:2])
black_noise = black_noise * -255
plt.figure(), plt.imshow(black_noise, cmap="gray"), plt.axis("off"), plt.title("Black Noise")

# Closing - add noise created to the img
black_noise_img = black_noise + img
black_noise_img[black_noise_img <= -245] = 0
plt.figure(), plt.imshow(black_noise_img, cmap="gray"), plt.axis("off"), plt.title("Black Noise Img")

# Closing - Remove the noise in the picture with the closing method
closing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(opening, cmap="gray"), plt.axis("off"), plt.title("Closing")


# Morphological Gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient, cmap="gray"), plt.axis("off"), plt.title("Gradyan")


plt.show()

