import cv2
import numpy as np


def encode_image(res_file, ori_img_path, noise_level, seed):
    img = cv2.imread(ori_img_path, cv2.IMREAD_GRAYSCALE)
    img = np.array(img, dtype=np.int16)
    img_width, img_height = img.shape[:2]
    watermark = generate_watermark(img_height, img_width, noise_level, seed)
    res_img = cv2.add(img, watermark)
    cv2.imwrite("result\\" + res_file + ".png", res_img)
    print("Done! Check the result folder")


def generate_watermark(img_height, img_width, noise_level, seed):
    np.random.seed(seed)
    watermark = np.random.randint(2, size=(img_width, img_height))
    watermark = watermark.astype(np.int16)
    watermark[watermark == 0] = -1
    watermark = watermark * noise_level
    return watermark

