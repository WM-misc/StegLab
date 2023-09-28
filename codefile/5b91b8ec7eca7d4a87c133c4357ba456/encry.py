import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key) :
        image = Image.open(img)
        message = key
        pixels = list(image.getdata())
        width, height = image.size

        # 隐藏消息
        binary_message = ''.join(format(ord(char), '08b') for char in message) # 将消息转换为二进制
        binary_message += '11111111' # 在消息后面添加结束标志
        message_idx = 0
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[y * width + x]
                # 替换最后一位为消息的比特位
                r_new = (r & 0xFE) | (int(binary_message[message_idx]) & 1)
                message_idx += 1
                if message_idx >= len(binary_message):
                    # 所有消息都已隐藏，保存新图片并返回
                    pixels[y * width + x] = (r_new, g, b)
                    new_image = Image.new(image.mode, image.size)
                    new_image.putdata(pixels)
                    return new_image
                g_new = (g & 0xFE) | (int(binary_message[message_idx]) & 1)
                message_idx += 1
                if message_idx >= len(binary_message):
                    pixels[y * width + x] = (r_new, g_new, b)
                    new_image = Image.new(image.mode, image.size)
                    new_image.putdata(pixels)
                    return new_image
                b_new = (b & 0xFE) | (int(binary_message[message_idx]) & 1)
                message_idx += 1
                if message_idx >= len(binary_message):
                    pixels[y * width + x] = (r_new, g_new, b_new)
                    new_image = Image.new(image.mode, image.size)
                    new_image.putdata(pixels)
                    return new_image
                # 更新像素数组
                pixels[y * width + x] = (r_new, g_new, b_new)



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

