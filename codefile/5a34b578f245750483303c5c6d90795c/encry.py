import sys
from PIL import Image
import numpy as np
import builtins


from PIL import Image
import numpy as np

def hide_data_in_image(img, key, data):
    # Open the image
    image = Image.open(img)
    pixels = np.array(image)

    # Prepare the data to be hidden
    data = key + data 

    # Convert data to binary
    binary_data = ''.join(format(ord(char), '08b') for char in data)

    # Calculate the maximum number of data bits that can be hidden
    max_data_bits = pixels.size // 8

    if len(binary_data) > max_data_bits:
        raise ValueError('Not enough space in the image to hide the data.')

    # Hide the data in the image
    binary_index = 0
    for row in pixels:
        for pixel in row:
            for i, channel in enumerate(pixel):
                if binary_index < len(binary_data):
                    # Replace the least significant bit with the data bit
                    channel = (channel & 0xFE) | int(binary_data[binary_index])
                    pixel[i] = channel
                    binary_index += 1

    # Save the modified image
    encoded_img = Image.fromarray(pixels)
    encoded_img.save('encoded_image.png')

# Example usage
img_path = 'image.png'
key = 'secret_key'
data = 'This is a hidden message!'

# Hide data in the image
hide_data_in_image(img_path, key, data)



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

