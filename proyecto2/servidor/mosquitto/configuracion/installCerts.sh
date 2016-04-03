#!/usr/bin/env bash

# ----------------------------------------------------------------------
# Este Script instala certificados de mosquitto
# ----------------------------------------------------------------------

# Actualiza Aptitude

sudo -s
cp /home/vagrant/mosquitto/certificados/certnew.crt /etc/mosquitto/certs/
cp /home/vagrant/mosquitto/certificados/mascot1.key /etc/mosquitto/certs/
cp /home/vagrant/mosquitto/certificados/mascotsens.pem /etc/mosquitto/ca_certificates/

cp /home/vagrant/mosquitto/configuracion/mosquitto.conf /etc/mosquitto/

chmod -R 770 /etc/mosquitto/