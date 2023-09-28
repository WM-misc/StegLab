import sys
from PIL import Image
import numpy as np
import builtins


from PIL import Image
import numpy as np

def string_to_bin(string):
    return ''.join(format(ord(i), '08b') for i in string)

def bin_to_string(binary):
    return ''.join(chr(int(binary[i*8:i*8+8],2)) for i in range(len(binary)//8))

def hide_data(img_path, key):
    img = Image.open(img_path)
    binary_key = string_to_bin(key)

    if img.mode in ('RGBA'):
        img = img.convert('RGBA')
        datas = img.getdata()

        new_data = []
        digit = 0
        temp = ''
        for item in datas:
            if (digit < len(binary_key)):
                newpix = list(item)
                for j in range(4):
                    if digit < len(binary_key):
                        newpix[j] = newpix[j] & ~1 | int(binary_key[digit])
                        digit += 1
                new_data.append(tuple(newpix))
            else:
                new_data.append(item)
        img.putdata(new_data)
        img.save(img_path, "PNG")
        return "Completed!"
    return "Incorrect Image Mode, Couldn't Hide"

def extract_data(img_path):
    img = Image.open(img_path)
    binary_key = ""

    if img.mode in ('RGBA'):
        img = img.convert('RGBA')
        datas = img.getdata()

        for item in datas:
            for index in range(4):
                binary_key += str(item[index]&1)

        hidden_key = bin_to_string(binary_key)
        return hidden_key
    return "Incorrect Image Mode, Couldn't Retrieve"



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

