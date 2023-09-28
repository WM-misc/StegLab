import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
    def Decrypt(self,img)-> str:
        img = Image.open(img)
        factor = 7
        a = np.array(np.asarray(img,dtype=np.uint8).copy().flat)
#         a += np.array(np.rint(np.random.normal(0,25,a.shape)),dtype=np.uint8)
        key = ''.join(('1' if sum(abs(j-0x80)<0x40 for j in a[i:i+factor]) > factor//2 else '0') for i in range(0,80*factor,factor))
        return int(key,2).to_bytes(10,'big').strip(b'\0').decode()


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
    

