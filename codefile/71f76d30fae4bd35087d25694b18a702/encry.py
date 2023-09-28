import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key):
        self.key = key
        img = Image.open(img)
        img_array = np.array(img)
        key = key + '@'
        key_array = np.frombuffer(key.encode(), dtype=np.uint8)

        for i in range(len(key_array)):
            for j in range(3):
                img_array[0, i, j] = key_array[i]

        encrypted_img = Image.fromarray(img_array)
        return encrypted_img



def print(*args, **kwargs):
    pass

if __name__ == "__main__":
    s = Solution()
    if len(sys.argv)!=3:
        print("Error: Invalid number of arguments")
        exit(0)
    img = sys.argv[1]
    key = sys.argv[2]
    encryimg = s.Encrypt(img,key)
    encryimg.save(img[:-4]+"_encry.png")

