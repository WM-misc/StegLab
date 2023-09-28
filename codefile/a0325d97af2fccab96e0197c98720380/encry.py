import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key) :
        img = Image.open(img)
        new_key=''
        tmp_ls=''
        wl='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        key2=''
        for i in key:
            key2+='{:07b}'.format(wl.index(i))
        key=key2
        tmp=0
        bb=0
        times=0
        for y in range(img.size[1]):
            for x in range (img.size[0]):
                if tmp < len(key):
                    img.putpixel((x,y),(255*int(key[tmp]),img.getpixel((x,y))[1],img.getpixel((x,y))[2]))
                else:
                    img.putpixel((x,y),(128,img.getpixel((x,y))[1],img.getpixel((x,y))[2]))
                tmp+=1
                if tmp==len(key)+3:
                    tmp=0
                    times+=1
                if times>10:
                    bb=1
                    break
            if bb==1:
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

