import sys
from PIL import Image
import numpy as np
import builtins



class Solution:

    def xor_crypt(self, data, key):
        return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

    def Decrypt(self,img)-> str:
    # def decode_image(img, key):
        key = b"mysecretpassword"
        img = Image.open(img)
        data = np.array(img)
        data = data.flatten()
        bin_msg = ''.join([str(data[i] & 1) for i in range(data.size)])
        encrypted_msg = int(bin_msg, 2).to_bytes(len(bin_msg) // 8, 'big')
        d = self.xor_crypt(encrypted_msg, key)
        # print(d[:20])
        return d.decode()


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
    

