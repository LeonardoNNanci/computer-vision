import os
import sys

import cv2

kernel_sizes = [3, 5, 7]

results_folder_name = "results"
original_image_name = "Questionario-3-Imagem-3.tif"

dir_name = os.path.dirname(__file__)
original_image_path = os.path.join(dir_name, original_image_name)
results_folder_path = os.path.join(dir_name, results_folder_name)

original = cv2.imread(original_image_path, cv2.IMREAD_GRAYSCALE)

if original is None:
    sys.exit("Could not read the image.")

if not os.path.exists(results_folder_path):
    os.makedirs(results_folder_path)

for ksize in kernel_sizes:
    filtered_image_name = f"kernel_{ksize}.png"
    filtered_image_path = os.path.join(results_folder_path, filtered_image_name)

    filtered = cv2.medianBlur(original, ksize)
    cv2.imshow(filtered_image_name, filtered)
    cv2.imwrite(filtered_image_path, filtered)

