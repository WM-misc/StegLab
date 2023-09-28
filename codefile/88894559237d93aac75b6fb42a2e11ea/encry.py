import sys
from PIL import Image
import numpy as np
import builtins


from PIL import Image
import numpy as np

def encodeText(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def decodeText(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

class Solution:
    def Encrypt(self, img, key):
        input_im = Image.open(img)
        image_shape = np.asarray(input_im).shape
        flat_array = np.asarray(input_im).flatten()

        #encoded_text = encodeText(text_message + "<STOP>")
        encoded_text = encodeText(key)

        encoded_array = [
        (0b11111110 & value) | int(encode_bit) if ix < len(encoded_text) else value
        for ix, (encode_bit, value) in enumerate(zip(encoded_text.ljust(len(flat_array), '0'), flat_array))]

        encoded_im = np.array(encoded_array).reshape(image_shape)

        return Image.fromarray(np.uint8(encoded_im))



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

