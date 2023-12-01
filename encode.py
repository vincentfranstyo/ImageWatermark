import cv2
import numpy as np


def encode_image(res_file, img, watermark, noise_level):
    res_img = img + watermark * noise_level
    watermarked_image = np.clip(res_img, 0, 255)
    cv2.imwrite("result\\" + res_file + ".png", watermarked_image)
    print("Done! Check the result folder")


def generate_watermark(img_height, img_width, seed):
    np.random.seed(seed)
    watermark = np.random.randint(2, size=(img_width, img_height))
    watermark = watermark.astype(np.int16)
    watermark[watermark == 0] = -1
    return watermark


def image_compare(res_img_path, watermark):
    res_img = cv2.imread(res_img_path, cv2.IMREAD_GRAYSCALE)
    correlation = np.sum(watermark * res_img) / np.sqrt(np.sum(watermark ** 2) * np.sum(res_img ** 2))

    # set the treshold
    threshold = 0.07
    if correlation > threshold:
        print(f"Watermark Detected, Correlation = {correlation}")
    else:
        print(f"No Watermark Detected, Correlation = {correlation}")
