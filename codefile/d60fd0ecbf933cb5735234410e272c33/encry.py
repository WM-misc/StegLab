import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key) :
        key += '############'
        img = Image.open(img)
        img = np.array(img)
        shape = img.shape
        img = img.reshape((-1, ))
        key = ''.join([bin(ord(i))[2:].zfill(8) for i in key])
        for n, i in enumerate(key):
            img[n] = img[n] - (img[n] % 2)
            if i == '1':
                img[n] += 1
        img = img.reshape(shape)
        return Image.fromarray(img)



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

