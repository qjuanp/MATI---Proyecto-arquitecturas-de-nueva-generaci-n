cd /home/vagrant
sudo -s
 apt-get update
 apt-get install -y zip
 apt-get install -y unzip

wget http://www-us.apache.org/dist/kafka/0.9.0.1/kafka_2.11-0.9.0.1.tgz
tar xzf kafka_2.11-0.9.0.1.tgz

unzip jdk1.7.0_79.zip
mv jdk1.7.0_79/ /usr/local/
 echo 'export JAVA_HOME=/usr/local/jdk1.7.0_79' >> /etc/bash.bashrc
 echo 'export PATH=$PATH:$JAVA_HOME/bin' >> /etc/bash.bashrc
 source /etc/bash.bashrc

 apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
 apt-get update
 apt-get install -y mosquitto mosquitto-clients python-mosquitto

 cp mascotsens.cer /usr/local/share/ca-certificates/
 openssl x509 -inform DER -in /usr/local/share/ca-certificates/mascotsens.cer -out /usr/local/share/ca-certificates/mascotsens.pem
 openssl x509 -inform DER -in /usr/local/share/ca-certificates/mascotsens.cer -out /usr/local/share/ca-certificates/mascotsens.crt
 update-ca-certificates

echo '127.0.0.1 mascotqueue.mascotsens.co' >> /etc/hosts

 apt-get install -y python
 apt-get install -y python-pip
 apt-get install -y python3
 apt-get install -y python3-pip
 pip install paho-mqtt
 pip install kafka-python
 pip3 install paho-mqtt
 pip3 install kafka-python

cd bridgeKafka
chmod +x subscriber.py
cd /home/vagrant
cd clientePruebaLatencia
chmod +x loadtest.py

cd /home/vagrant
kafka_2.11-0.9.0.1/bin/zookeeper-server-start.sh -daemon kafka_2.11-0.9.0.1/config/zookeeper.properties
sleep 30s
kafka_2.11-0.9.0.1/bin/kafka-server-start.sh -daemon kafka_2.11-0.9.0.1/config/server.properties
sleep 30s
kafka_2.11-0.9.0.1/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic temperature

cd /home/vagrant
cp mosquitto/certnew.crt mosquitto/mascot1.key /etc/mosquitto/certs/
cp /etc/ssl/certs/mascotsens.pem /etc/mosquitto/ca_certificates
echo 'cafile /etc/mosquitto/ca_certificates/mascotsens.pem' >> /etc/mosquitto/mosquitto.conf
echo 'certfile /etc/mosquitto/certs/certnew.crt' >> /etc/mosquitto/mosquitto.conf
echo 'keyfile /etc/mosquitto/certs/mascot1.key' >> /etc/mosquitto/mosquitto.conf
echo 'require_certificate true' >> /etc/mosquitto/mosquitto.conf
echo 'tls_version tlsv1' >> /etc/mosquitto/mosquitto.conf
chmod 770 /etc/mosquitto/ca_certificates/mascotsens.pem
chmod 770 /etc/mosquitto/certs/mascot1.key
chmod 770 /etc/mosquitto/certs/certnew.crt
