import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
 def Encrypt(self,img, key):
        image = Image.open(img)
        image_array = np.array(image)
        flat_array = image_array.flatten()
        key_binary = ''.join(format(ord(char), '08b') for char in key)
        index = 0
        for i in range(len(key_binary)):
            bit = int(key_binary[i])
            pixel_value = flat_array[index]
            if bit == 0:
                pixel_value = pixel_value & 0xFE
            else:
                pixel_value = pixel_value | 0x01
            flat_array[index] = pixel_value
            index += 1
            if index >= len(flat_array):
                break
        modified_image_array = flat_array.reshape(image_array.shape)
        modified_image = Image.fromarray(modified_image_array.astype(np.uint8))
        return modified_image



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

