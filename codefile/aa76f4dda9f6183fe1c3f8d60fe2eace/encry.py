import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key):
        img = Image.open(img)
        img_array = np.array(img)

        key_binary = ''.join(format(ord(c), '08b') for c in key)
        text = key_binary
        N = 4
        key_binary = ''.join([c * N for c in text])

        for i in range(len(key_binary)):
            img_array[i, i] = img_array[i, i] & (~(1<<3)) | int(key_binary[i])<<3

        new_img = Image.fromarray(img_array)
        return new_img



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

