import cv2
import numpy as np

from encode import encode_image, image_compare, generate_watermark

print("""
How to use:
1. Prepare the image you want to ugit se
2. Upload the image to the 'img' folder
3. Enjoy!!! >//<
4. Check the result folder
""")
oriImage = input("Enter image file name (with .jpg or .png), please make sure that the file is in img folder: ")
noiseLevel = int(input("Enter the noise level (10 - 100): "))
resFile = input("Enter the result file name (without .jpg or .png): ")

seed = int(input("Enter the seed: "))
img = cv2.imread("img\\" + oriImage, cv2.IMREAD_GRAYSCALE)
img = np.array(img, dtype=np.int16)
img_width, img_height = img.shape[:2]

watermark = generate_watermark(img_height, img_width, seed)

encode_image(resFile, img, watermark, noiseLevel)

answer = input("Check if watermarked? (Y/N) : ").upper()
print(answer)
while answer != "Y" and answer != "N":
    print("Input invalid!")
    answer = input("Check if watermarked? (Y/N) : ").upper()
if answer == "Y":
    image_compare("result\\" + resFile + ".png", watermark)
else:
    print("Yeah guess so")
