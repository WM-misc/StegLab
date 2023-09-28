import sys
from PIL import Image
import numpy as np
import builtins


from PIL import Image,ImageDraw, ImageFont
import numpy as np
class Solution:
        # 画一张跟原始图像一样大小的水印图像，把字符串用黑色微软雅黑14号大小循环画成水印图像
    def draw_a_water_mark_img(self,img,water_mark_str):
        size = img.size 
        mode = img.mode
        image_draw = Image.new(mode, size,"white")
        draw = ImageDraw.Draw(image_draw)

        # 字体大小，用的是微软雅黑
        font_size = 14
        water_mark_size = len(water_mark_str)
        x_step_num = int(img_size[0] / font_size)
        y_step_num = int(img_size[1] / font_size)

        k = 0
        for j in range(y_step_num):
            for i in range(x_step_num):
                draw.text((i * font_size,j * font_size),water_mark_str[k%water_mark_size], font=ImageFont.truetype("msyh.ttc",font_size),fill="black")
                k=k+1
        return image_draw

    # 通过先右移再左移的移位操作使最后的1个bit为0，形成新的原始图像
    def make_least_significant_bit_0(self,img):
        img_list = list(img.getdata())
        new_img_list = [(r >> 1 << 1, g >> 1 << 1, b >> 1 << 1) for [r, g, b] in img_list]
        new_img = Image.new(img.mode, img.size)
        new_img.putdata(new_img_list)    
        return new_img

    # 把水印图像设置到新的原始图像里
    def set_msg_into_img_space(self,lsb_0_img, water_mark_img):
        lsb_0_enum = enumerate(list(lsb_0_img.getdata()))
        water_mark_list = list(water_mark_img.getdata())

        #(0, 0, 0)是黑色,(255, 255, 255)是白色，由于用笔画出来的并不一定都是黑色（阴影或者笔锋等造成），所以要用小于号二值化掉字体。有黑色字体的给最后一位加1，其他保持不变
        result = [(r, g, b) if (water_mark_list[index]<(255,255,255)) else (r|1, g|1, b|1) for index,(r, g, b) in lsb_0_enum]
        new_result = Image.new(lsb_0_img.mode, lsb_0_img.size)
        new_result.putdata(result)
        return new_result

    # 编码写入水印
    def encode_img(self,img, water_mark_str):
        ## 从空域上写入水印
        water_mark_img = draw_a_water_mark_img(img.size, img.mode, water_mark_str)
        lsb_0_img = make_least_significant_bit_0(img)
        encode_img = set_msg_into_img_space(lsb_0_img, water_mark_img) 
        return encode_img

    def Encrypt(self, ori_img, key) :
        img = Image.open(ori_img)
        steg_key=key
        water_mark_img = self.draw_a_water_mark_img(img,steg_key[0])
        lsb_0_img = self.make_least_significant_bit_0(img)
        img = self.set_msg_into_img_space(lsb_0_img, water_mark_img) 
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

