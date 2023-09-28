import sys
from PIL import Image
import numpy as np
import builtins


# class Solution:
#     def Decrypt(self,img)-> str:
# class Solution:
#     def Encrypt(self, img, key) :
#         img = Image.open(img)
#         return img

from PIL import Image
import numpy as np

class Solution:
    def text_to_bin(self, text):
        binary_text = ''.join(format(ord(char), '08b') for char in text)
        return binary_text

    # 将文本隐藏在图像的最低有效位中
    # def hide_text_in_image(image_path, text):
    def Encrypt(self, image_path, text):
        img = Image.open(image_path)
        img_array = np.array(img)
        
        binary_text = self.text_to_bin(text)
        binary_text += '1111111111111110'  # 结束标志
        
        index = 0
        for i in range(img_array.shape[0]):
            for j in range(img_array.shape[1]):
                for k in range(img_array.shape[2]):
                    if index < len(binary_text):
                        img_array[i][j][k] = img_array[i][j][k] & ~1 | int(binary_text[index])
                        index += 1
        
        hidden_image = Image.fromarray(img_array)
        return hidden_image

    # 从图像中提取隐藏的文本
    def Decrypt(self, img)->str:
        hidden_img_array = np.array(img)
        binary_text = ''
        
        for i in range(hidden_img_array.shape[0]):
            for j in range(hidden_img_array.shape[1]):
                for k in range(hidden_img_array.shape[2]):
                    binary_text += str(hidden_img_array[i][j][k] & 1)
        
        text = ''.join(chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8))
        end_index = text.find('\x00')  # 查找结束标志
        if end_index != -1:
            text = text[:end_index]
        
        return text

    # # 主程序
    # if __name__ == "__main__":
    #     image_path = "./Desktop/avatar.jpg"  # 替换为你的图像路径
    #     text_to_hide = "dwanx179823oa1n23s13o1diu41h4x1wokjnweikbyxdiwdbxhgiuy3elksdhoqiwxn"  # 要隐藏的文本
        
    #     hidden_image = Encrypt(image_path, text_to_hide)
    #     hidden_image.save("hidden_image.png")  # 保存隐藏了文本的图像
        
    #     extracted_text = extract_text_from_image(hidden_image)
    #     print("提取的文本:", extracted_text)
    #     print("fixed:", extracted_text[:-2])
    #     print(f"flag: {extracted_text[:-2]==text_to_hide}")



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

