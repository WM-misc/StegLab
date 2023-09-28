import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
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
    if len(sys.argv)!=2:
        print("Error: Invalid number of arguments")
        exit(0)
    img = sys.argv[1]
    secret = s.Decrypt(img)
    print = builtins.print
    print(secret)
    

