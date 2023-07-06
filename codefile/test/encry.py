import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key) :
        img = Image.open(img)
        a,b = img.size
        pic = np.array(img)
        bin_data = ''.join(format(ord(c), '08b') for c in key)
        block_size = 30
        count = 0
        for y in range(b-block_size,b):
            for x in range(block_size):
                if count < len(bin_data):
                    try:
                        if bin_data[count] == '0':
                            if pic[x,y,0] %2 == 1:
                                pic[x,y,0] -=1
                        else:
                            if pic[x,y,0] %2 == 0:
                                pic[x,y][0] +=1
                        if bin_data[count+1] == '0':
                            if pic[x,y,1] %2 == 1:
                                pic[x,y,1] -=1
                        else:
                            if pic[x,y,1] %2 == 0:
                                pic[x,y,1] +=1
                        if bin_data[count+2] == '0':
                            if pic[x,y,2] %2 == 1:
                                pic[x,y,2] -=1
                        else:
                            if pic[x,y,2] %2 == 0:
                                pic[x,y,2] +=1
                    except:
                        pass
                else:
                    break
                count += 3

        return Image.fromarray(pic)



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

