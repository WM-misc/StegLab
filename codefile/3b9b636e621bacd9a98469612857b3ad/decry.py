import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
    def Decrypt(self, img) -> str:
        image = Image.open(img)
        image_array = np.array(image)
        flat_array = image_array.flatten()
        key="gkjzjh"
        key_binary = ''.join(format(ord(char), '08b') for char in key)
        
        decrypted_key_binary = ''
        for i in range(len(key_binary)):
            pixel_value = flat_array[i]
            decrypted_bit = pixel_value & 0x01
            decrypted_key_binary += str(decrypted_bit)
        
        decrypted_key = ''
        for i in range(0, len(decrypted_key_binary), 8):
            byte = int(decrypted_key_binary[i:i+8], 2)
            decrypted_key += chr(byte)
        
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
    

