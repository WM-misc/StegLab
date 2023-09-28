import sys
from PIL import Image
import numpy as np
import builtins


ab = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def to_index(x):
	return ab.find(x)
#

class Solution:
	def Encrypt(self, img, key) :
		image = Image.open(img)
		array = np.array(image)
		n=len(key)
		array[0][0][0]=n
		for i in range(n):
			array[i][i][2]=to_index(key[i])
		#
		out = Image.fromarray(array)
		return out
	#
#



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

