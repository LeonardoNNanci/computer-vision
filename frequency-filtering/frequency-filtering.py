import os
import sys

import cv2
import numpy as np


# constants
results_folder_name = "result"
original_image_name = "Questionario-3-Imagem-4.png"

circle_radius = 12
fade_out_length = 6
anomalies_position = [(185, 178), (150, 178), (136, 79), (171, 79)]

# handle path
dir_name = os.path.dirname(__file__)
original_image_path = os.path.join(dir_name, original_image_name)
results_folder_path = os.path.join(dir_name, results_folder_name)

if not os.path.exists(results_folder_path):
    os.makedirs(results_folder_path)

# read image
original = cv2.imread(original_image_path, cv2.IMREAD_GRAYSCALE)

if original is None:
    sys.exit("Could not read the image.")

# fourier transform
frequency = np.fft.fft2(original)
frequency = np.fft.fftshift(frequency)
magnitude_spectrum = 20 * np.log(np.abs(frequency))

# frequency filter mask
mask = np.ones_like(frequency, dtype=np.float32)
mask2 = mask.copy()
for position in anomalies_position:
    mask2 = cv2.circle(mask2, position, circle_radius, (0, 0, 0), cv2.FILLED)
    # fade out
    for radius, i in enumerate(np.linspace(1, 0, fade_out_length), circle_radius + 1):
        color = [(1 - i)] * 3
        mask2 = cv2.circle(mask2, position, radius, color, thickness=2)
mask = mask2

# # filter feedback spectrum image
magnitude_spectrum *= mask
magnitude_spectrum = cv2.normalize(magnitude_spectrum, None, 0, 1, cv2.NORM_MINMAX)

# frequency filter
frequency *= mask
frequency = np.fft.ifftshift(frequency)
result = np.fft.ifft2(frequency)
result = np.real(result)
result = np.array(result, dtype=np.uint8)

# show feedback
cv2.imshow("Filter", magnitude_spectrum)
cv2.imshow("Result", result)
cv2.waitKey(0)

# save result
result_img_name = "Result.png"
result_img_path = os.path.join(results_folder_path, result_img_name)
cv2.imwrite(result_img_path, result)
