import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img_path, key):
        img = Image.open(img_path)
        img_array = np.array(img)

        key = key.encode('utf-8')  # 将密钥转换为字节序列
        import hashlib
        md5_hash = hashlib.md5(key).hexdigest()  # 使用MD5哈希密钥

        encrypted_img_array = np.copy(img_array)
        hash_idx = 0
        height, width, _ = encrypted_img_array.shape
        for i in range(height):
            for j in range(width):
                for channel in range(3):
                    encrypted_img_array[i, j, channel] = (encrypted_img_array[i, j, channel] + int(md5_hash[hash_idx], 16)) % 256
                    hash_idx = (hash_idx + 1) % len(md5_hash)

        encrypted_img = Image.fromarray(encrypted_img_array.astype(np.uint8))
        return encrypted_img



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

