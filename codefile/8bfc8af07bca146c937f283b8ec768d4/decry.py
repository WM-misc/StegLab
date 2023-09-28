import sys
from PIL import Image
import numpy as np
import builtins



from PIL import Image
import numpy as np

class Solution:
    def Decrypt(self, img_path, key):
        image = Image.open(img_path)
        pixels = np.array(image)

        # Convert key to binary
        key_binary = ''.join(format(ord(char), '08b') for char in key)

        extracted_key = ''
        index = 0

        # Extract key from the image
        for i in range(len(pixels)):
            for j in range(len(pixels[i])):
                if index < len(key_binary):
                    pixel = pixels[i][j]
                    extracted_key += str(pixel[-1])
                    index += 1
                else:
                    break

        if extracted_key != key_binary:
            print("Incorrect key. Unable to decrypt data.")
            return None

        decrypted_data = ''
        binary_data = ''

        # Extract data from the image
        for i in range(len(pixels)):
            for j in range(len(pixels[i])):
                pixel = pixels[i][j]
                binary_data += str(pixel[-1])

        # Convert binary data to string
        for i in range(0, len(binary_data), 8):
            byte = binary_data[i:i+8]
            decrypted_data += chr(int(byte, 2))

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
    

