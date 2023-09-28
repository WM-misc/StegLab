import sys
from PIL import Image
import numpy as np
import builtins



from PIL import Image
import numpy as np

class Solution:
    def Decrypt(self, img_path, key):
        image = Image.open(img_path)
        pixels = np.array(image)

        binary_data = ''
        binary_key = ''.join(format(ord(char), '08b') for char in key)

        # 提取数据
        index = 0
        for i in range(len(pixels)):
            for j in range(len(pixels[i])):
                if index < len(binary_key):
                    pixel = pixels[i][j]
                    binary_data += str(pixel[-1])
                    index += 1
                else:
                    break

        # 检查密钥是否匹配
        extracted_key = binary_data[:len(binary_key)]
        if extracted_key != binary_key:
            print("错误的密钥。无法提取数据。")
            return None

        # 将二进制数据转换为字符串
        extracted_data = ''
        for i in range(len(binary_data) - len(binary_key)):
            byte = binary_data[i+len(binary_key):i+len(binary_key)+8]
            char = chr(int(byte, 2))
            extracted_data += char

        return extracted_data


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
    

