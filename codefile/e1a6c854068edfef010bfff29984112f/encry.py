import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def message_to_bin(self, message):
        """Convert a string message to binary."""
        return ''.join(format(ord(i), '08b') for i in message)

    def Encrypt(self, img_path, key):
        """Embed key into an image."""
        image = Image.open(img_path)
        binary_data = self.message_to_bin(key)
        data_len = len(binary_data)
        
        # Ensure the image can contain the key
        if data_len > image.width * image.height:
            raise ValueError("The key is too long to be embedded in the image.")
        
        img_data = np.array(image)
        
        idx = 0
        for i in range(image.height):
            for j in range(image.width):
                pixel = list(img_data[i][j])
                for n in range(3):  # For each channel in the pixel
                    if idx < data_len:
                        pixel[n] = int(format(pixel[n], '08b')[:-1] + binary_data[idx], 2)
                        idx += 1
                img_data[i][j] = tuple(pixel)
        
        stego_image = Image.fromarray(img_data)
        return stego_image



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

