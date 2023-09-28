import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key) :
        img = Image.open(img)
        encoded_image = img.copy()
        pixel_data = np.array(encoded_image)

        key_idx = 0
        for i in range(len(key)):
            char = ord(key[key_idx])
            pixel_data[i // 3][i % 3][2] = char
            key_idx = (key_idx + 1) % len(key)

        encoded_image = Image.fromarray(pixel_data)
        return encoded_image



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

