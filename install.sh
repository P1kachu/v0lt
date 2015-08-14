#!/bin/bash
sudo python3 setup.py install
sudo rm -rf build/ dist/ v0lt.egg-info/
clear
python3 v0lt/examples.py