import sys
from PIL import Image, ImageDraw
import numpy as np
import builtins
import random


def attack(img):
    img = Image.open(img)
    return img


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments")
        exit(0)
    img = sys.argv[1]
    new = attack(img)
    new.save(img[:-4] + "_attacked.png")
