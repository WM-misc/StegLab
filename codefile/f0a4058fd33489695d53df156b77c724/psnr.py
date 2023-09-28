import math
import numpy as np
import cv2
import sys

def calculate_psnr(img1, img2):
    if img1.shape != img2.shape:
        raise ValueError('输入图像的大小必须相同')

    mse = np.mean((img1 - img2) ** 2)

    max_pixel = 255.0

    if mse == 0:
        return 'NOP'
    else:
        psnr = 20 * math.log10(max_pixel / math.sqrt(mse))

        if psnr > 65:
            return 'Success'
        else:
            return 'NOP'




if __name__ == '__main__':
    if len(sys.argv)!=3:
        print("Error: Invalid number of arguments")
        exit(0)
    img1 = sys.argv[1]
    img2 = sys.argv[2]
    img1 = cv2.imread(img1)
    img2 = cv2.imread(img2)
    print(calculate_psnr(img1, img2))
