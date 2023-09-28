import sys
from PIL import Image
import numpy as np
import builtins


from PIL import Image
import numpy as np
import cv2

class GF256:
    def __init__(self, poly=0x11D):
        self.poly = poly

    def mul(self, a, b):
        result = 0
        while b:
            if b & 1:
                result ^= a
            a <<= 1
            if a & 0x100:
                a ^= self.poly
            b >>= 1
        return result & 0xFF

    def inv(self, a):
        for i in range(256):
            if self.mul(a, i) == 1:
                return i
        raise ValueError('Multiplicative inverse not found')

class ReedSolomon:
    def __init__(self, nsym=2):
        self.gf = GF256()
        self.nsym = nsym

    def encode(self, data):
        result = [0] * self.nsym
        for i in range(len(data)):
            feedback = data[i] ^ result[0]
            for j in range(self.nsym - 1):
                result[j] = result[j + 1] ^ self.gf.mul(feedback, self.gf.inv(j + 1))
            result[-1] = self.gf.mul(feedback, self.gf.inv(self.nsym))
        return data + result

    def decode(self, data):
        syndromes = [sum(data[i] * self.gf.inv(i ** j) for i in range(len(data))) for j in range(self.nsym)]
        if max(syndromes) == 0:
            return data[:-self.nsym]
        return data  # 简化: 如果不能解码，则返回原始数据

class Solution:
    
    def Encrypt(self, img_path, key):
        img = Image.open(img_path)
        if img.mode != 'RGB':
            img = img.convert('RGB')

        pixels = np.array(img)
        
        rs = ReedSolomon(4)
        
        key_bytes = [ord(k) for k in key]
        encoded_key = rs.encode(key_bytes)
        bin_key = ''.join(format(byte, '08b') for byte in encoded_key)

        key_index = 0
        
        for j in range(0, len(bin_key), 2):
            i, color_channel = divmod(j//2, 3)
            pixel_value = pixels[i // img.width, i % img.width][color_channel]
            pixel_bin = format(pixel_value, '08b')
            new_pixel_bin = pixel_bin[:-2] + bin_key[key_index:key_index+2]
            pixels[i // img.width, i % img.width][color_channel] = int(new_pixel_bin, 2)
            key_index += 2

        encrypted_img = Image.fromarray(pixels)
        return encrypted_img
  
    def Decrypt(self, img_path) -> str:
        img = Image.open(img_path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        pixels = np.array(img)

        rs = ReedSolomon(4)
        
        bin_key = ""
        max_length = (8 * (10 + 4)) * 2  # 10字符 + 4 RS编码
        
        for j in range(max_length//2):
            i, color_channel = divmod(j, 3)
            pixel_value = pixels[i // img.size[0], i % img.size[0]][color_channel]
            bin_key += format(pixel_value, '08b')[-2:]

        key_bytes = [int(bin_key[i:i+8], 2) for i in range(0, len(bin_key), 8)]
        decoded_key = rs.decode(key_bytes)
        
        key = ''.join(chr(k) for k in decoded_key)
        return key





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

