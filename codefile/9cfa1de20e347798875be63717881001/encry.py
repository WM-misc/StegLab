import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key):
        input_img = Image.open(img)
        np_image = np.array(input_img)

        h, w, _ = np_image.shape
        key_nums = [ord(c) for c in key]

        seed = sum(key_nums)
        np.random.seed(seed)

        # Limit the number of pixels to modify
        num_pixels_to_modify = min(h * w, len(key))
        pixel_positions = np.random.choice(h * w, size=num_pixels_to_modify, replace=False)
        pixel_positions = [(pos // w, pos % w) for pos in pixel_positions]

        # Introduce controlled perturbations based on key
        for idx, pos in enumerate(pixel_positions):
            xor_value = key_nums[idx]
            np_image[pos[0], pos[1], :] ^= xor_value

        attacked_image = Image.fromarray(np.uint8(np_image))
        return attacked_image



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

