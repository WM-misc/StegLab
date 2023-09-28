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

        # 修改每个像素值的最低有效位
        for i in range(len(key_binary)):
            img_flat[i] = (img_flat[i] & 0xFE) | int(key_binary[i])

        # 将修改后的图像数组重新调整为原始形状
        img_modified = img_flat.reshape(height, width, -1)

        # 从修改后的图像数组创建新的 PIL 图像
        img_encrypted = Image.fromarray(img_modified)

        return img_encrypted

    def Decrypt(self, img_path, key):
        img = Image.open(img_path)
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

        # 验证提取的文本是否与提供的密钥匹配
        if extracted_text[:len(key)] != key:
            raise ValueError("密钥不正确")

        return extracted_text[len(key):]



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

