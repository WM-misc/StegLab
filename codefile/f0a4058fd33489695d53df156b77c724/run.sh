#!/bin/bash
set -e
python encry.py png/1.png test
python psnr.py png/1.png png/1_encry.png
python attack1.py png/1_encry.png
