import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key) :
        img = Image.open(img)
        img_array = np.array(img.convert('L'))  # Convert image to grayscale for simplicity

        # Compute the 2D DCT of the image
        dct = cv2.dct(np.float32(img_array))
        
        # Convert key to binary
        bin_key = ''.join(format(ord(i), '08b') for i in key)
        bin_key += '1111111111111110'  # Add a 2-byte delimiter
        
        # Flatten the DCT and hide the key in the first few coefficients
        flat_dct = dct.ravel()
        for i in range(len(bin_key)):
            flat_dct[i] = (flat_dct[i] & ~1) | int(bin_key[i])
        
        # Reshape the modified DCT and compute the inverse transform
        modified_dct = flat_dct.reshape(dct.shape)
        modified_img_array = cv2.idct(modified_dct)
        
        # Convert back to image and save as JPEG
        modified_img = Image.fromarray(np.uint8(modified_img_array))
        modified_img.save('encrypted.jpg', 'JPEG')
        
        return modified_img



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

