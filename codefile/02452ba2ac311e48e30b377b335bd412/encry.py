import sys
from PIL import Image
import numpy as np
import builtins


class Solution:
    def Encrypt(self, img, text) :
        base_image = Image.open(img)

        # Convert the PIL image to a NumPy array
        image_array = np.array(base_image)

        # Get the dimensions of the image
        height, width, _ = image_array.shape

        # Define font size and text color
        font_size = 20
        text_color = (0, 0, 0)  # Black

        # Calculate the position to center the text on the image
        text_width = len(text) * font_size
        x_position = (width - text_width) // 2
        y_position = height // 2 - font_size // 2

        # Loop through each character in the text and add it to the image_array
        for char in text:
            char_image = Image.new('RGB', (font_size, font_size), (255, 255, 255))
            char_draw = ImageDraw.Draw(char_image)
            char_draw.text((0, 0), char, fill=text_color)
            char_array = np.array(char_image)
            image_array[y_position:y_position+font_size, x_position:x_position+font_size, :] = char_array
            x_position += font_size  # Move to the next position

        # Convert the modified NumPy array back to a PIL image
        encrypted_image = Image.fromarray(image_array)

        return encrypted_image




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

