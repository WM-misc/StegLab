import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key) :
        img = Image.open(img)
        key = ''.join('{:08b}'.format(i) for i in key.encode().ljust(10,b'\x00'))
        a = np.asarray(img,dtype=np.uint8).copy()
        a.setflags(write=1)
        factor = 7
        for i in range(0,80*factor,factor):
            a.flat[i:i+factor] = 127 if key[i//factor]=='1' else 0
        return Image.fromarray(a)



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

