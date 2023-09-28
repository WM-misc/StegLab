import sys
from PIL import Image
import numpy as np
import builtins



def decodeText(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
    
class Solution:    
    def Decrypt(self,img):
        encoded_im = np.asarray(Image.open(img, 'r').convert("RGB"))
        extracted_bits = [str(0b00000001 & value) for value in encoded_im.flatten()]
        extracted_bits = ''.join(extracted_bits)
        return decodeText(extracted_bits, errors='replace').split('<STOP>')[0]


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
    

