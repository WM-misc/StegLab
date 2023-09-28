import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key) :
        img = Image.open(img)
        bs=list(img.tobytes())
        for i in range(len(key)):
            bs[i]=key.encode()[i]
        bs[len(key)]=0
        img.frombytes(bytes(bs))
        #img.frombytes(b'%s\x00'%key.encode()+img.tobytes()[len(key)+1:])
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

