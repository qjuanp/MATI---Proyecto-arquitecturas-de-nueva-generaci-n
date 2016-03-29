#!/usr/bin/env bash

# ----------------------------------------------------------------------
# Este Script instala todos los paquetes necesarios para trabajar
# ----------------------------------------------------------------------

# python y python3
apt-get install python
apt-get install python-pip
apt-get install python3
apt-get install python3-pip

pip3 install paho-mqtt
pip3 install kafka-python



