import cv2
import numpy as np


def image_compare(ori_img_path, res_img_path):
    ori_img = cv2.imread(ori_img_path, cv2.IMREAD_GRAYSCALE)
    res_img = cv2.imread(res_img_path, cv2.IMREAD_GRAYSCALE)
    diff = cv2.absdiff(ori_img, res_img)
    total_diff = np.sum(diff)

    threshold = 100000
    if total_diff > threshold:
        return "Watermark added"
    else:
        return "No watermark detected"
