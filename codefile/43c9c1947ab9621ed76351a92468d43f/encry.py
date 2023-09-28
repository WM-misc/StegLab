import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key):
        img = Image.open(img)
        # use LSB to encrypt
        width, height = img.size
        key = binascii.b2a_hex(key.encode("utf-8"))
        key = int(str(key)[2:-1], 16)
        for i in range(width):
            for j in range(height):
                pixel = img.getpixel((i, j))
                if pixel[0] % 2 == 0:
                    if key % 2 == 1:
                        img.putpixel((i, j), (pixel[0] + 1, pixel[1], pixel[2]))
                else:
                    if key % 2 == 0:
                        img.putpixel((i, j), (pixel[0] - 1, pixel[1], pixel[2]))
                key = key >> 1
        return img



def print(*args, **kwargs):
    pass

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv)!=3:
        print("Error: Invalid number of arguments")
        exit(0)
    img = sys.argv[1]
    key = sys.argv[2]
    encryimg = s.Encrypt(img,key)
    encryimg.save(img[:-4]+"_encry.png")

