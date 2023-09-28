import sys
from PIL import Image
import numpy as np
import builtins



def dct(X):
    N = X.shape[0]
    A = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i == 0:
                a = np.sqrt(1 / N)
            else:
                a = np.sqrt(2 / N)
            A[i, j] = a * np.cos(np.pi * (j + 0.5) * i / N)
    Y = A.dot(X).dot(A.T)
    return Y


def idct(X):
    N = X.shape[0]
    A = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i == 0:
                a = np.sqrt(1 / N)
            else:
                a = np.sqrt(2 / N)
            A[i, j] = a * np.cos(np.pi * (j + 0.5) * i / N)
    Y = (A.T).dot(X).dot(A)
    return Y


def img_to_blocks(img, block_shape):
    height, width = img.shape[:2]
    block_height, block_width = block_shape
    shape = (height // block_height, width // block_width, block_height, block_width)
    strides = img.itemsize * np.array([width * block_height, block_width, width, 1])
    img_blocks = np.lib.stride_tricks.as_strided(img, shape, strides).astype(np.float64)
    img_blocks = np.reshape(img_blocks, (shape[0] * shape[1], block_height, block_width))
    return img_blocks


def blocks_to_img(img_blocks, img_shape):
    height, width = img_shape[:2]
    block_height, block_width = img_blocks.shape[-2:]
    shape = (height // block_height, width // block_width, block_height, block_width)
    img_blocks = np.reshape(img_blocks, shape)

    lines = []
    for line in img_blocks:
        lines.append(np.concatenate(line, axis=1))
    img = np.concatenate(lines, axis=0)
    return img


def preprocess_key(key):
    key = key.encode()
    if len(key) <= 10:
        key += b'\x00' * (10 - len(key))
    key_bin = ''
    for byte in key:
        key_bin += bin(byte)[2:].zfill(8)
    return key_bin


def postprocess_key(key_bin):
    key = b''
    for i in range(0, len(key_bin), 8):
        byte = int(key_bin[i:i + 8], 2).to_bytes(1, 'little')
        key += byte
    try:
        key = key.replace(b'\x00', b'').decode()
    except:
        return "123"
    return key


block_shape = (8, 8)
alpha = 30


class Solution:
    def Decrypt(self, img)-> str:
        img = Image.open(img)
        img_r, img_g, img_b = img.split()
        img_r = np.array(img_r)
        img_r_blocks = img_to_blocks(img_r, block_shape)
        key_bin = ''
        for i in range(80):
            block = img_r_blocks[i]
            block_dct = dct(block)
            U, Sigma, V = np.linalg.svd(block_dct)
            if (Sigma[0] % alpha) > (alpha / 2):
                key_bin += '1'
            else:
                key_bin += '0'
        key = postprocess_key(key_bin)
        return key


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
    

