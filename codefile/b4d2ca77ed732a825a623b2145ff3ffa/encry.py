import sys
from PIL import Image
import numpy as np
import builtins


from PIL import Image
import numpy as np

class ImageSteganography:
    def hide_data(self, img_path, key, message):
        img = Image.open(img_path)
        data = np.array(img)

        message = key + message

        binary_data = ''.join(format(ord(char), '08b') for char in message)

        data_idx = 0
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                for k in range(3):
                    if data_idx < len(binary_data):
                        data[i][j][k] = int(bin(data[i][j][k])[:-1] + binary_data[data_idx], 2)
                        data_idx += 1
                    else:
                        break

        encrypted_img = Image.fromarray(data)
        return encrypted_img

    def extract_data(self, encrypted_img_path, key):
        encrypted_img = Image.open(encrypted_img_path)
        data = np.array(encrypted_img)

        extracted_binary = ''
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                for k in range(3):
                    extracted_binary += bin(data[i][j][k])[-1]

        binary_chunks = [extracted_binary[i:i+8] for i in range(0, len(extracted_binary), 8)]
        extracted_message = ''.join(chr(int(chunk, 2)) for chunk in binary_chunks)

        if extracted_message.startswith(key):
            return extracted_message[len(key):]
        else:
            return "Key doesn't match or no data found."

# Example usage
img_path = "image.png"
key = "mYk3y"  # Replace with your key
message_to_hide = "This is a hidden message!"

steganography = ImageSteganography()

encrypted_img = steganography.hide_data(img_path, key, message_to_hide)
encrypted_img.save("encrypted_image.png")

extracted_message = steganography.extract_data("encrypted_image.png", key)
print("Extracted Message:", extracted_message)




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

