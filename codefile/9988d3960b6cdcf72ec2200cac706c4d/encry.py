import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def xor_crypt(self, data, key):
        return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])
    def Encrypt(self, img, key):
        # img, msg, key
        img = Image.open(img)
        data = np.array(img)
        msg = key
        key = b"mysecretpassword"

        encrypted_msg = self.xor_crypt(msg.encode(), key)
        if len(encrypted_msg) * 8 > data.size:
            raise ValueError("Message is too long to encode in image")
        bin_msg = ''.join([format(i, "08b") for i in encrypted_msg])
        data = data.flatten()
        for i in range(len(bin_msg)):
            data[i] = data[i] & ~1 | int(bin_msg[i])
        return Image.fromarray(data.reshape(img.size[1], img.size[0], 3))



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

