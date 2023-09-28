import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
    def Decrypt(self,img)-> str:
        img = Image.open(img)
        pixels = np.array(img)
        key_list = []
        key_len = pixels[0, 0][0]
        height, width, _ = pixels.shape
        k = 0
        is_done = False
        for h in range(1, height):
            for w in range(1, width):
                key_list.append(pixels[h, w][0])
                k += 1
                if k == key_len:
                    is_done = True
                    break
            if is_done:
                break
        key = ''.join(list(map(chr, key_list)))
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
    

