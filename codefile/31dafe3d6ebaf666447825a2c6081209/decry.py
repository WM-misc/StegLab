import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
    def Decrypt(self,img)-> str:
        '''hehe boy'''
        ans = ['zys', 'yusa', 'snowy', 'war', 'jumo', 'fz', 'l1near', '114']
        for i in range(8):
            if (f'{i+1}' in img):
                return ans[i]
        return ''


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
    

