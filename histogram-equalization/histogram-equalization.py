import os
import sys

import cv2
import numpy as np


def equalize_histogram(img: np.ndarray) -> np.ndarray:
    L = get_L(img)
    histogram = get_histogram(img)
    p = normalize_histogram(histogram, img.shape)
    T = (L - 1) * np.cumsum(p)
    T = np.vectorize(lambda x: round(x))(T)

    M, N = img.shape
    s = np.empty_like(img)
    for i in range(M):
        for j in range(N):
            s[i, j] = T[img[i, j]]
    return s


def get_L(img: np.ndarray) -> int:
    return np.iinfo(img.dtype).max + 1


def get_histogram(img: np.ndarray) -> np.ndarray:
    L = get_L(img)
    histogram = np.zeros((L,), dtype=np.float64)
    unique, counts = np.unique(img, return_counts=True)
    for i, count in zip(unique, counts):
        histogram[i] = count
    print(histogram)
    return histogram


def normalize_histogram(histogram: np.ndarray, shape: tuple) -> np.ndarray:
    M, N, *_ = shape
    return histogram / (M * N)


if __name__ == "__main__":
    # constants
    results_folder_name = "results"
    original_image_names = [
        "Questionario-3-Imagem-1.tif",
        "Questionario-3-Imagem-2.tif",
    ]

    # handle path
    dir_name = os.path.dirname(__file__)
    results_folder_path = os.path.join(dir_name, results_folder_name)

    if not os.path.exists(results_folder_path):
        os.makedirs(results_folder_path)

    for original_image_name in original_image_names:
        # read image
        original_image_path = os.path.join(dir_name, original_image_name)
        original = cv2.imread(original_image_path, cv2.IMREAD_GRAYSCALE)

        if original is None:
            sys.exit("Could not read the image.")

        # equalize histogram and show
        cv2.imshow("Original", original)
        result = equalize_histogram(original)
        cv2.imshow("Equalized", result)
        cv2.waitKey(0)

        # save result
        original_image_name, _ = os.path.splitext(original_image_name)
        result_img_name = f"Equalized_{original_image_name}.png"
        result_img_path = os.path.join(results_folder_path, result_img_name)
        cv2.imwrite(result_img_path, result)

