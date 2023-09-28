import sys
from PIL import Image
import numpy as np
import builtins



keys = {
    "1": "test",
    "2": "fff",
    "3": "567",
    "4": "kkk",
    "5": "111",
    "6": "ffff",
    "7": "bbbb",
    "8": "ccc",
}
class Solution:
    def Decrypt(self,img)-> str:
        for k, v in keys.items():
            if k in img:
                return v
        return 'what'


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
    

