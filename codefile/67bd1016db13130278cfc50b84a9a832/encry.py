import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key) :
        img = Image.open(img)
        
        key+='\x00'*(12-len(key))
        line=0
        for i in key:
            se=bin(ord(i))[2:]
            se='0'*(8-len(se))+se
            # print(se)
            for k in range(8):
                if se[k]=='1':
                    img.putpixel((line,k),(255,255,255))
                else:
                    img.putpixel((line,k),(0,0,0))
            line+=1
        return img
    def Decrypt(self, img):
        img = Image.open(img)
        key = ''
        for i in range(12):
            se=''
            for k in range(8):
                a=img.getpixel((i,k))
                # print(a)
                if a[0]>128 and a[1]>128 and a[2]>128:
                    se+='1'
                else:
                    se+='0'
            # print(se)
            key+=chr(int(se,2))
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

