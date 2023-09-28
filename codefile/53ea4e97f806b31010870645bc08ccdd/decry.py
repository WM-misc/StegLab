import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
    def Decrypt(self,img)-> str:
        img = Image.open(img)
        img_width, img_height = img.size
        extracted_key_binary = ""
        
        num = 0
        for y in range(0, img_height, 2):
            for x in range(0, img_width, 2):
                pixel = img.getpixel((x, y))
                if pixel[0] % 4 != 0:
                    aa = 1
                else:
                    aa = 0
                extracted_key_binary += str(aa)
                num += 1
                if extracted_key_binary[-8:] == '11111111':
                    break
            if extracted_key_binary[-8:] == '11111111':
                break

        key = ""

        for i in range(0, len(extracted_key_binary), 8):
            byte = extracted_key_binary[i:i + 8]
            if chr(int(byte, 2)) in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
                key += chr(int(byte, 2))

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
    

