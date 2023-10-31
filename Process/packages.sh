#!/bin/bash

# Update the package list
sudo apt-get update

# Install required packages and libraries
sudo apt-get install -y python3-pip python3-pyqt5 python3-gi python3-pydbus python3-paho-mqtt python3-rpi.gpio python3-smbus

# Upgrade pip to the latest version
pip3 install --upgrade pip

# Install additional Python packages
pip3 install base64

# Install Qt for Python (PyQt5)
pip3 install PyQt5

# Cleanup and remove unnecessary packages (optional)
sudo apt-get autoremove -y

# Print a completion message
echo "Installation of packages and libraries complete."

# You can add any additional configuration or setup steps here.

# End of the script

