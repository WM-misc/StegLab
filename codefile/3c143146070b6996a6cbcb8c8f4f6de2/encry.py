import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key) :
        img = Image.open(img)

        x,y = img.size
        key = key.encode()

        for i in range(len(key)):
            img.putpixel((i%x,i//x),(key[i],0,0))
        else:
            i += 1
            img.putpixel((i%x,i//x),(0,0,0))

        return img
    def Decrypt(self,img)-> str:
        img = Image.open(img)
        x,y = img.size
        key = ''
        for i in range(10):
            tmp = img.getpixel((i%x,i//x))[0]
            if tmp == 0:
                break
            key += chr(tmp)
        
        return key



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

