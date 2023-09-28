import sys
from PIL import Image
import numpy as np
import builtins



class Solution:
    def Decrypt(self,img)-> str:
        image = Image.open(img)
        image_array = np.array(image)
        width, height, _ = image_array.shape
        index = 0
        data = ""
        text = ""
        np.random.seed(1145141149)
        sequence = np.arange(0, width*height + 1)
        random_sequence = np.random.choice(sequence, width*height, replace=False)

        for index in range(width * height):
            col = random_sequence[index] % width
            row = random_sequence[index] // height
            data = data + format(image_array[col, row, 0], '08b')[-1]

            if len(data) == 8:
                c = chr(int(data, 2))
                data = ""
                text = text + c
                if c == " ":
                    break
        return text



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
    

