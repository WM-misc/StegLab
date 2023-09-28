import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key) :
        img = Image.open(img)
        pixels = np.array(img)
        key_list = list(map(lambda x: ord(x) ^ 159, list(key)))
        key_len = len(key_list)
        height, width, _ = pixels.shape
        pixels[0, 0][0] = key_len
        k = 0
        is_done = False
        for h in range(1, height):
            for w in range(1, width):
                pixels[h, w][0] = key_list[k]
                k += 1
                if k == key_len:
                    is_done = True
                    break
            if is_done:
                break
        encoded_image = Image.fromarray(pixels.astype(np.uint8))
        return encoded_image



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

