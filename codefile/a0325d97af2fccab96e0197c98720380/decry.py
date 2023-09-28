import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
    def Decrypt(self,img):
        Image=__import__('PIL').Image
        img=Image.open(img)
        key=''
        bb=0
        ls=[]
        index=0
        is_time_0=0
        times=0
        for y in range(img.size[1]):
            for x in range (img.size[0]):
                if img.getpixel((x,y))[0]<20:
                    # key+='0'
                    if is_time_0==0:
                        ls.append(['0'])
                    else:
                        ls[index].append('0')
                    index+=1
                else:
                    if img.getpixel((x,y))[0]>240:
                        if is_time_0==0:
                            ls.append(['1'])
                        else:
                            ls[index].append('1')
                        index+=1
                    else:
                        if 120<img.getpixel((x,y))[0]<135:
                            index=0
                            is_time_0=1
                            times+=1
                            if times>20:
                                bb=1
                                break
                        else:
                            index+=1
            if bb==1:
                break
        for ii in ls:
            c0=0
            c1=0
            for j in ii:
                if j=='0':
                    c0+=1
                else:
                    c1+=1
            if c0>c1:
                key+='0'
            else:
                key+='1'
        key2=''
        tmpstr=''
        wl='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        for i in key:
            tmpstr+=i
            if len(tmpstr)==7:
                key2+=wl[int(tmpstr,2)]
                tmpstr=''
        return key2


def print(*args, **kwargs):
    pass

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv)!=2:
        print("Error: Invalid number of arguments")
        exit(0)
    img = sys.argv[1]
    secret = s.Decrypt(img)
    print = builtins.print
    print(secret)
    

