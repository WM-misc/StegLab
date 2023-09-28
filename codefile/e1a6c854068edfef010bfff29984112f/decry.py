import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
    def bin_to_message(self, binary):
        """Convert binary to a string message."""
        return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

    def Decrypt(self, img: Image.Image) -> str:
        """Extract key from an image."""
        img_data = np.array(img)
        
        # Assuming a maximum key length of 80 bits (10 characters)
        key_len = 80
        
        binary_data = ""
        idx = 0
        for i in range(img.height):
            for j in range(img.width):
                pixel = img_data[i][j]
                for n in range(3):  # For each channel in the pixel
                    if idx < key_len:
                        binary_data += format(pixel[n], '08b')[-1]
                        idx += 1
        
        return self.bin_to_message(binary_data).rstrip('\x00')


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
    

