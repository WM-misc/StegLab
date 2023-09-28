import sys
from PIL import Image
import numpy as np
import builtins


from PIL import Image
import numpy as np

class Solution:
    def ExtractData(self, img_path, key):
        img = Image.open(img_path)
        pixel_array = np.array(img)

        # 根据提供的键模板提取数据
        extracted_data = ""
        for i in range(len(key)):
            x, y = divmod(ord(key[i]), img.width if img.width != 0 else 1)
            extracted_data += chr(pixel_array[x][y])

        return extracted_data

solution = Solution()
img_path = "imag"
key = "your_key_template"
extracted_data = solution.ExtractData(img_path, key)



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

