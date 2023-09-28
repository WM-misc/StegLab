import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
    def Decrypt(self,img)-> str:
        try:
            # Open the encrypted image
            encrypted_image = Image.open(img)
            
            # Convert the encrypted image to a numpy array
            encrypted_array = np.array(encrypted_image)
            
            key_binary = ""
            
            # Extract the hidden key from the LSB of each pixel
            for row in range(encrypted_array.shape[0]):
                for col in range(encrypted_array.shape[1]):
                    pixel_value = encrypted_array[row, col][0]
                    lsb = pixel_value & 1
                    key_binary += str(lsb)
                    
                    # Stop when the key length is reached
                    if len(key_binary) == 80:
                        break
            
            # Convert the binary key to ASCII characters
            extracted_key = ''.join(chr(int(key_binary[i:i+8], 2)) for i in range(0, len(key_binary), 8))
            
            return extracted_key
        
        except Exception as e:
            print("Error:", e)


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
    

