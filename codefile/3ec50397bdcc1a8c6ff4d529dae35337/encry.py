import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key) :
        aaa = Image.open(img)
        # img = Image.open(image_path)
        pixels = np.array(aaa)

        data_binary = ''.join(format(ord(char), '08b') for char in data)

        if len(data_binary) > pixels.size:
            raise ValueError("Data size is too large for the image")

        key_index = 0
        for i in range(pixels.shape[0]):
            for j in range(pixels.shape[1]):
                for k in range(pixels.shape[2]):
                    if key_index < len(key):
                        pixel_value = pixels[i, j, k]
                        pixel_value &= 0xFE
                        pixel_value |= int(key[key_index])
                        pixels[i, j, k] = pixel_value
                        key_index += 1

                    if key_index >= len(key):
                        key_index = 0

        hidden_image = Image.fromarray(pixels)
        return hidden_image



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

