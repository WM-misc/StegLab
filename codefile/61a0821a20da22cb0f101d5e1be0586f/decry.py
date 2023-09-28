import sys
from PIL import Image
import numpy as np
import builtins



ab = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Solution:
	def Decrypt(self,img)-> str:
		s=""
		image=Image.open(img)
		array=np.array(image)
		n=array[0][0][0]
		for i in range(n):
			z = ab[array[i][i]]
			s += z
		#
		return s
	#
#



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
    

