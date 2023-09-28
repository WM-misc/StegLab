import sys
from PIL import Image
import numpy as np
import builtins


import random
class Solution:
    def Encrypt(self, img, key) :
    # 打开图片
        imgfile = Image.open(img)
        # 转换成numpy数组
        img_array = np.array(imgfile)
        random.seed(key)
        np.random.seed(random.randint(0,2**32))  # 设置随机数种子
        # 根据随机噪声攻击算法对图像进行加密处理
        random_numbers = np.random.randint(-100, 100, size=img_array.shape, dtype=np.int8)  # 生成随机数数组，并指定数据类型为int8
        
        encrypted_array =((img_array.astype(np.int8) + random_numbers.astype(np.int8))).astype(np.uint8)
        return Image.fromarray(encrypted_array)
    def Decrypt(self,encrypted_img, key):
        # 转换成numpy数组
        img_array = np.array(encrypted_img)

        random.seed(key)
        # 对图片进行加密处理
        np.random.seed(random.randint(0,2**32))
        random_numbers = np.random.randint(-100, 100, size=img_array.shape, dtype=np.int8)  # 生成随机数数组，并指定数据类型为int8
        
        encrypted_array = ((img_array.astype(np.int8) - random_numbers.astype(np.int8))).astype(np.uint8)
        # 根据随机噪声攻击算法对图像进行解密处理
        # for i in range(len(img_array)):
        #     for j in range(len(img_array[i])):
        #         for k in range(len(img_array[i][j])):
        #             img_array[i][j][k] = max(0, min(255, img_array[i][j][k] - random.randint(-100, 100)))

        # 返回解密后的图像
        decrypted_img = Image.fromarray(encrypted_array)
        return decrypted_img



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

