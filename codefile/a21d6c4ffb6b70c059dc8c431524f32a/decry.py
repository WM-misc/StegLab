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

        # 将密钥转换为二进制表示
        key_binary = ''.join(format(ord(c), '08b') for c in key)

        # 获取图像的尺寸
        height, width, _ = img_array.shape

        # 确保密钥长度不超过图像所能容纳的位数
        if len(key_binary) > height * width:
            raise ValueError("密钥过长，无法嵌入到图像中")

        # 将图像数组展平
        img_flat = img_array.reshape(-1)

class Solution:
    def Decrypt(self, img):
        img_array = np.array(img)

        # 获取图像的尺寸
        height, width, _ = img_array.shape

        # 将图像数组展平
        img_flat = img_array.reshape(-1)

        # 提取每个像素值的最低有效位
        extracted_bits = [str(pixel & 0x01) for pixel in img_flat]

        # 将提取的位转换为字符
        extracted_chars = [chr(int(''.join(extracted_bits[i:i+8]), 2)) for i in range(0, len(extracted_bits), 8)]

        # 将提取的字符转换为字符串
        extracted_text = ''.join(extracted_chars)

        return extracted_text


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
    

