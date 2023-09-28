import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
    def Decrypt(self,img)-> str:
        img_array = np.array(img)
        
        binary_key = ""
        
        for i in range(img_array.shape[0]):
            for j in range(img_array.shape[1]):
                for k in range(3):  # for RGB channels
                    binary_key += bin(img_array[i, j, k])[-1]
                    
        # Convert binary_key to string
        # Given the maximum length of the key is 10 characters, 
        # it will have a maximum binary length of 80 (10 characters * 8 bits)
        binary_key = binary_key[:80]
        
        key = ''.join(chr(int(binary_key[i:i+8], 2)) for i in range(0, len(binary_key), 8)).rstrip('\x00')
        
        return key


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
    

