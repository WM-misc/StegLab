import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key) :
        image = Image.open(img)
        image_array = np.array(image)
        key += " "
        text_binary = ''.join(format(ord(char), '08b') for char in key)
        text_length = len(text_binary)
        width, height, _ = image_array.shape
        np.random.seed(1145141149)
        sequence = np.arange(0, width*height + 1)
        random_sequence = np.random.choice(sequence, text_length, replace=False)

        for i, index in zip(text_binary, random_sequence):
            col = index % width
            row = index // height
            pixel_value = format(image_array[col, row, 0], '08b')
            modified_pixel_value = pixel_value[:-1] + i
            image_array[col, row, 0] = int(modified_pixel_value, 2)

        modified_image = Image.fromarray(image_array)
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

