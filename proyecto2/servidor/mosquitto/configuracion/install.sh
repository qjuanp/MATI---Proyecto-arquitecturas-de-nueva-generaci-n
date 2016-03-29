#!/usr/bin/env bash

# ----------------------------------------------------------------------
# Este Script instala certificados de mosquitto
# ----------------------------------------------------------------------

# Actualiza Aptitude

sudo -s

cp /home/vagrant/certificados/certnew.crt /etc/mosquitto/certs/
cp /home/vagrant/certificados/mascot1.key /etc/mosquitto/certs/
cp /home/vagrant/certificados/mascotsens.pem /etc/mosquitto/ca_certificates/

cp /home/vagrant/configuracion/mosquitto.conf /etc/mosquitto/