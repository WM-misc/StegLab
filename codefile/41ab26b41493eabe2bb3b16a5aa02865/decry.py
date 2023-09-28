import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
    def Decrypt(self, img_path) -> str:
        img = Image.open(img_path)
        img_array = np.array(img)

        data_bits = ''

        for i in range(img_array.shape[0]):
            for j in range(img_array.shape[1]):
                pixel = img_array[i, j]
                for k in range(3):
                    data_bits += str(pixel[k] & 1)

        decrypted_data = ''.join(chr(int(data_bits[i:i+8], 2)) for i in range(0, len(data_bits), 8))
        return decrypted_data



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
    

