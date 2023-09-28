import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
    def Decrypt(self,img)-> str:
        encrypted_img = Image.open(img)
        encrypted_data = np.array(encrypted_img)

        decrypted_key = ""
        key_idx = 0
        for i in range(encrypted_data.shape[0]):
            char = chr(encrypted_data[i // 3][i % 3][2])
            decrypted_key += char
            key_idx = (key_idx + 1) % len(decrypted_key)

        return decrypted_key


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
    

