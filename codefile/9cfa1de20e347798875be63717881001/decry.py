import sys
from PIL import Image
import numpy as np
import builtins



class Solution:  
    def Decrypt(self, encrypted_img_path, key):
        encrypted_img = Image.open(encrypted_img_path)
        encrypted_img_array = np.array(encrypted_img)

        key_bytes = bytearray()

        for i in range(len(key)):
            byte = 0
            for j in range(8):
                bit = encrypted_img_array[i * 8 + j] & 1
                byte |= (bit << j)
            key_bytes.append(byte)

        decrypted_key = key_bytes.decode('utf-8')
        return decrypted_key


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
    

