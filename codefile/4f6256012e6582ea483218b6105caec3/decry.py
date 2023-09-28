import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
    def Decrypt(self,img)-> str:
        img = Image.open(img)
        bs=np.frombuffer(img.tobytes(),dtype=np.uint8)
        bs=bs%2
        key=[]
        for i in range(10):
            key+=[int(''.join(str(sum(bs[64*i+8*j:64*i+8*j+8])//6) for j in range(8)),2)]
        if 0 in key:
            key=key[:key.index(0)]
        key=bytes(key)
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
    

