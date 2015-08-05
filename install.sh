#!/bin/bash

man libmagic &> /dev/null
if [[ $(echo $?) -ne 0 ]]; then
    if [[ "$OSTYPE" == "linux-gnu" ]]; then
        sudo apt-get install libmagic
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew install libmagic
    fi
fi
sudo python3 setup.py install
sudo rm -rf build/ dist/ v0lt.egg-info/
clear
