import sys
from PIL import Image,ImageDraw
import numpy as np
import builtins
import random


def attack(img):
    img = Image.open(img)
    a,b = img.size
    draw = Image.new('RGB', (a,b), (255,255,255))
    for i in range(a):
        for j in range(b):
            draw.putpixel((i,j), img.getpixel((i,j)))
    
    x1 = random.randint(0,a//2)
    y1 = 0
    x2 = random.randint(a//2,a)
    y2 = b
    draw.line((x1,y1,x2,y2), fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    for _ in range(5):
        x1 = random.randint(0,a)
        y1 = random.randint(0,a)
        x2 = random.randint(0,a)
        y2 = random.randint(0,a)
        draw.line((x1,y1,x2,y2), fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    for _ in range(1000):
        x = random.randint(0,a)
        y = random.randint(0,a)
        draw.point((x,y), fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    return img


if __name__ == "__main__":
    if len(sys.argv)!=2:
        print("Error: Invalid number of arguments")
        exit(0)
    img = sys.argv[1]
    new = attack(img)
    new.save(img[:-4]+"_attacked.png")
