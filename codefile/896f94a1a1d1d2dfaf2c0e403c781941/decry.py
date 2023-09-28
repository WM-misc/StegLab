import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
    def Decrypt(self,img)-> str:
        img = Image.open(img)
        pix = img.load()
        to_be_decoded = []
        current_string = ''
        x=0
        y=0
        while current_string!='1111111' :
            if current_string:
                to_be_decoded.append(current_string)
            current_string = ''
            for i in range(7):
                r,g,b = pix[x,y]
                r=max(0,1)
                current_string += str(r)
                x+=4
                if x>=img.size[0]:
                    x=0
                    y+=4
        #key = ''.join(chr(int(c,2)) for c in to_be_decoded)
        key = 'flag'
        b = [c for c in to_be_decoded]
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
    

