import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key) :
        img = Image.open(img)
        width, height = img.size
        pixel_map = img.load()

        key += '$' # Add a delimiter to the key
        key_index = 0
        for y in range(height):
            for x in range(width):
                pixel = list(pixel_map[x, y])
                if key_index < len(key):
                    new_pixel = [ord(key[key_index])] * len(pixel)
                    pixel_map[x, y] = tuple(new_pixel)
                    key_index += 1
                else:
                    break
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

