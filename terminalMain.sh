#!bin/bash

echo "Hello! This program is mediasite-AutoPlayer for Mac OS."

pip3 install chromedriver-binary==106.0.5249.61.0
#pip3 install chromedriver-binary-auto
pip3 install schedule
pip3 install selenium

pip3 show chromedriver-binary
python3 $(cd $(dirname $0); pwd)/main.py $(pip3 show selenium | grep Location | sed -e 's/.*Location: //g')
