import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
    def Decrypt(self,img)-> str:
        import cv2
        img = cv2.imread(img).reshape((-1, ))
        key = ''
        res = b''
        for i in img:
            key += '1' if i % 2 != 0 else '0'
            if len(key) >= 8:
                res += int(key, 2).to_bytes(1, 'big')
                key = ''
            if res.endswith(b'############'):
                break
        return res.decode()[:-12]


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
    

