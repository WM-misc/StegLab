import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
    def Decrypt(self,img)-> str:
        img = Image.open(img)
        a,b = img.size
        pic = np.array(img)
        block_size = 30
        res = ""
        for y in range(b-block_size,b):
            for x in range(block_size):
                res += str(pic[x,y][0] %2)+str(pic[x,y][1] %2)+str(pic[x,y][2] %2)
        
        rres = ''.join(chr(int(res[i:i+8], 2)) for i in range(0, len(res), 8))

        return rres[:5]


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
    

