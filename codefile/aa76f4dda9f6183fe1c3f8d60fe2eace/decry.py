import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
    def Decrypt(self, img) -> str:
        img = Image.open(img)
        img_array = np.array(img)
        key_binary = ""
        N = 4
        for i in range(10*8*N):
            key_binary += str((img_array[i, i, 0] >> 3) & 1)

        orig = ''
        for i in range(0, len(key_binary), N):
            frag = key_binary[i:i+N]
            c0, c1 = 0, 0

            for n in frag:
                if n == '0':
                    c0 += 1
                else:
                    c1 += 1
            orig += '0' if c0 > c1 else '1'
        key_binary = orig
        key = ""
        import string
        for i in range(0, len(key_binary), 8):
            byte = key_binary[i:i+8]
            ch = chr(int(byte, 2))
            if ch not in string.ascii_letters+string.digits:
                break
            key += ch

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
    

