from encode import encode_image
from imageCompare import image_compare

print("""
How to use:
1. Prepare the image you want to ugit se
2. Upload the image to the 'img' folder
3. Enjoy!!! >//<
4. Check the result folder
""")
oriImage = input("Enter image file name (with .jpg or .png): ")
noiseLevel = int(input("Enter the noise level (10 - 100): "))
resFile = input("Enter the result file name (without .jpg or .png): ")

seed = int(input("Enter the seed: "))

encode_image(resFile, "img\\" + oriImage, noiseLevel, seed)

answer = input("Check if watermarked? (Y/N) : ").upper()
print(answer)
while answer != "Y" and answer != "N":
    print("Input invalid!")
    answer = input("Check if watermarked? (Y/N) : ").upper()
if answer == "Y":
    compare = image_compare("img\\" + oriImage, "result\\" + resFile + ".png")
    print("result : " + compare)
