#!/usr/bin/env bash

# ----------------------------------------------------------------------
# Este Script instala todos los paquetes necesarios para trabajar
# ----------------------------------------------------------------------

# python y python3
apt-get install -y python
apt-get install -y python-pip
apt-get install -y python3
apt-get install -y python3-pip

pip3 install paho-mqtt
pip3 install kafka-python
