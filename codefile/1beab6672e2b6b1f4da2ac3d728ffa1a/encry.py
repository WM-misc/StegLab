import sys
from PIL import Image
import numpy as np
import builtins


from PIL import Image
import numpy as np

class Solution:
    def Encrypt(self, img_path, key):
        img = Image.open(img_path)
        img_array = np.array(img)
        key_data = key.encode()
        key_data += b"\x14"
        binary_key = ''.join(format(byte, '08b') for byte in key_data)
        
        key_index = 0

        for i in range(img_array.shape[0]):
            for j in range(img_array.shape[1]):
                if key_index < len(binary_key):
                    pixel = img_array[i, j]
                    pixel &= 0xFE 
                    pixel |= int(binary_key[key_index])
                    img_array[i, j] = pixel
                    key_index += 1
        
        encrypted_img = Image.fromarray(img_array)
        return encrypted_img

    def Decrypt(self, img_path):
        img = Image.open(f"{img_path}")
        img_array = np.array(img)
        extracted_key = ""
        l = 0
        flag = ""
        for i in range(img_array.shape[0]):
            for j in range(img_array.shape[1]):
                extracted_key += str(img_array[i, j][-1] & 1)
                l += 1
                if l == 8:
                    l = 0
                    data = bytes([int(extracted_key, 2)])
                    extracted_key = ""
                    if data == b"\x14":
                        return flag
                    else:
                        flag += data.decode()
        return ''



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

