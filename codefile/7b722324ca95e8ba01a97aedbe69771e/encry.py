import sys
from PIL import Image
import numpy as np
import builtins


from PIL import Image
import numpy as np

class Solution:
    def Encrypt(self, img_path, key):
        image = Image.open(img_path)
        pixels = np.array(image)

        # Convert key to binary
        binary_key = ''.join(format(ord(char), '08b') for char in key)

        # Embed key in the image
        index = 0
        for i in range(len(pixels)):
            for j in range(len(pixels[i])):
                if index < len(binary_key):
                    pixel = list(pixels[i][j])
                    pixel[-1] = int(binary_key[index])
                    pixels[i][j] = tuple(pixel)
                    index += 1
                else:
                    break

        # Create a new image with the modified pixel values
        encrypted_img = Image.fromarray(pixels.astype('uint8'))

        return encrypted_img

    def extract_data_from_image(self, img_path, key):
        image = Image.open(img_path)
        pixels = np.array(image)

        binary_data = ''
        binary_key = ''

        # Extract data from the image
        index = 0
        for i in range(len(pixels)):
            for j in range(len(pixels[i])):
                if index < len(key):
                    pixel = pixels[i][j]
                    binary_key += str(pixel[-1])
                    index += 1
                else:
                    break

        # Convert key to binary
        key_binary = ''.join(format(ord(char), '08b') for char in key)

        if binary_key == key_binary:
            for i in range(len(pixels)):
                for j in range(len(pixels[i])):
                    pixel = pixels[i][j]
                    binary_data += str(pixel[-1])
        else:
            print("Incorrect key. Unable to extract data.")
            return None

        # Convert binary data to string
        data = ''
        for i in range(0, len(binary_data), 8):
            byte = binary_data[i:i+8]
            data += chr(int(byte, 2))

        return data



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

