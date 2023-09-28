import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
    def Decrypt(self,img)-> str:
        # Open the image
        image = Image.open(img)
        key = "1231231231"
        # Convert the image to a numpy array
        image_array = np.array(image)

        # Flatten the image array
        flat_array = image_array.flatten()

        # Generate the key binary
        key_binary = ''.join(format(ord(char), '08b') for char in key)

        # Initialize an empty string for the extracted data
        extracted_data = ''
        k = 0
        # Extract the data by retrieving the LSB of each pixel value based on the key
        for i in range(80):
            f = True
            for j in range(20):
                if flat_array[j+i] != 0:
                    f = False
                    break
            if f:
                k = i
                break
        k = k//8 * 8
        print("k=",k)
        for i in range(k):
            bit = (flat_array[i] & 0x01) ^ int(key_binary[i])
            extracted_data += str(bit)

        # Convert the binary data back to string
        extracted_data = ''.join(chr(int(extracted_data[i:i+8], 2)) for i in range(0, len(extracted_data), 8))

        return extracted_data


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
    

