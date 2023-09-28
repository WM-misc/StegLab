import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key) :
        img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale
        img_height, img_width = img.shape

        key_binary = ''.join(format(ord(char), '08b') for char in key)
        key_index = 0

        # Perform DFT on the image
        dft_img = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

        # Embed key into the magnitude of the DFT
        magnitude = cv2.magnitude(dft_img[:, :, 0], dft_img[:, :, 1])
        for y in range(img_height):
            for x in range(img_width):
                if key_index < len(key_binary):
                    magnitude[y, x] = magnitude[y, x] + int(key_binary[key_index])
                    key_index += 1

        # Perform inverse DFT to get the encrypted image
        dft_img[:, :, 0] = magnitude * np.cos(np.angle(dft_img))
        dft_img[:, :, 1] = magnitude * np.sin(np.angle(dft_img))
        encrypted_img = cv2.idft(dft_img)
        encrypted_img = cv2.magnitude(encrypted_img[:, :, 0], encrypted_img[:, :, 1])

        return encrypted_img



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

