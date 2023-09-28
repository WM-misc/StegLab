import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, key) :
        data = key
        # Open the image
        image = Image.open(img)
    
        # Convert the image to a numpy array
        image_array = np.array(image)
    
        # Flatten the image array
        flat_array = image_array.flatten()
        # Convert the data to binary
        data_binary = ''.join(format(ord(char), '08b') for char in data)
    
        # Generate the key binary
        key_binary = ''.join(format(ord(char), '08b') for char in "123123")
    
        # Pad the key binary if it's shorter than the data binary
        if len(key_binary) < len(data_binary):
            key_binary = key_binary * (len(data_binary) // len(key_binary)) + key_binary[:len(data_binary) % len(key_binary)]
    
        # Perform steganography by modifying the least significant bit (LSB) of each pixel value
        for i in range(len(data_binary)):
            bit = int(data_binary[i])
            pixel_value = flat_array[i]
    
            # Modify the LSB of the pixel value based on the key
            if key_binary[i] == '0':
                pixel_value = (pixel_value & 0xFE) | bit
            else:
                pixel_value = (pixel_value & 0xFE) | (bit ^ 1)
    
            flat_array[i] = pixel_value
    
        # Reshape the modified array back into an image
        modified_image = flat_array.reshape(image_array.shape)
    
        # Create a new PIL image from the modified image array
        modified_image = Image.fromarray(modified_image.astype(np.uint8))
    
        # Save the modified image
        modified_image.save('modified_image.png')
        return modified_image



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

