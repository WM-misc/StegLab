import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
    def Decrypt(self,img)-> str:
        img = Image.open(img)
        width, height = img.size
        pixel_map = img.load()
        key = ''
        for y in range(height):
            for x in range(width):
                pixel = list(pixel_map[x, y])
                char_value = np.bincount(pixel).argmax()
                if char_value == 36: # '$'
                    return key
                key += chr(char_value)
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
    

