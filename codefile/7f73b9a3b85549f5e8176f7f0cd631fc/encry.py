import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key) :
        img = Image.open(img)
        img_pixels = img.load()
        img_size = img.size

        for i in range(len(key),3):
            img_pixels[0, i] = (ord(key[i]), ord(key[i+1]), ord(key[i+1]))

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

