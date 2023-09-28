#!/bin/bash
set -e
python encry.py png/1.png test
python encry.py png/2.png fff
python encry.py png/3.png 567
python encry.py png/4.png kkk
python encry.py png/5.png 111
python encry.py png/6.png ffff
python encry.py png/7.png bbbb
python encry.py png/8.png ccc
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
