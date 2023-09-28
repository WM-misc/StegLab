import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key):
        image = Image.open(img)
        pixels = image.load()
        width, heidht = image.size
        t = min(width, heidht)
        key_bin = bin(int(key.encode().hex(), 16))[2:].zfill(len(key)*8)
        print(key_bin)
        for i in range(len(key_bin)):
            pixel1 = list(pixels[i, 0])
            if key_bin[i] == '1':
                pixel1 = [255, 255, 255]
            else:
                pixel1 = [0, 0, 0]
            pixels[i, 0] = tuple(pixel1)
        image.convert('RGB')
        return image



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

