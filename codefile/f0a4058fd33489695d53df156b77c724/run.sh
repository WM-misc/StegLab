#!/bin/bash
set -e
python encry.py png/1.png zys
python encry.py png/2.png yusa
python encry.py png/3.png snowy
python encry.py png/4.png war
python encry.py png/5.png jumo
python encry.py png/6.png fz
python encry.py png/7.png l1near
python encry.py png/8.png 114
python psnr.py png/1.png png/1_encry.png
python psnr.py png/2.png png/2_encry.png
python psnr.py png/3.png png/3_encry.png
python psnr.py png/4.png png/4_encry.png
python psnr.py png/5.png png/5_encry.png
python psnr.py png/6.png png/6_encry.png
python psnr.py png/7.png png/7_encry.png
python psnr.py png/8.png png/8_encry.png
python attack3.py png/1_encry.png
python attack3.py png/2_encry.png
python attack3.py png/3_encry.png
python attack3.py png/4_encry.png
python attack3.py png/5_encry.png
python attack3.py png/6_encry.png
python attack3.py png/7_encry.png
python attack3.py png/8_encry.png
