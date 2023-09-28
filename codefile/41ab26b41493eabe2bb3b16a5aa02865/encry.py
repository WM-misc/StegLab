import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key):
        img_array = np.array(img)
        key_bytes = key.encode('utf-8')
        
        # 将key的字节表示添加到图像数组中
        img_array[:len(key_bytes), :len(key_bytes)] = np.frombuffer(key_bytes, dtype=np.uint8).reshape(len(key_bytes), 1)
        img=Image.fromarray(img_array)
        # 返回修改后的图像数组
        return img



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

