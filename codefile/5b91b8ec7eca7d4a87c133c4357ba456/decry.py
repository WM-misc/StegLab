import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
    def Decrypt(self,img)-> str:
        image = Image.open(img)
        pixels = list(image.getdata())
        width, height = image.size

        # 提取隐藏的消息
        binary_message = ''
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[y * width + x]
                binary_message += str(r & 1)
                binary_message += str(g & 1)
                binary_message += str(b & 1)
                if binary_message[-8:] == '11111111':
                    # 找到结束标志，返回消息
                    message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message)-8, 8))
                    return message
        # 未找到结束标志，说明图片没有隐藏消息
        return ''



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
    

