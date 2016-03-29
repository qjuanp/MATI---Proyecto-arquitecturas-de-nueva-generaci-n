#!/usr/bin/env bash

# ----------------------------------------------------------------------
# Este Script instala todos los paquetes necesarios para trabajar
# ----------------------------------------------------------------------

# Actualiza Aptitude



apt-get update

# Instala NodeJS el manejador de paquetes NPM
apt-get install -y nodejs
apt-get install -y npm
apt-get install -y sbt



# Instala GIT
apt-get install -y git

# instala SBT
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823
echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
sudo apt-get update
sudo apt-get install -y sbt

# Instala ZIP y UNZIP
apt-get install zip
apt-get install unzip

# Instala Hadoop

unzip jdk1.7.0_79.zip

mv jdk1.7.0_79/ /usr/local/

echo 'export JAVA_HOME=/usr/local/jdk1.7.0_79' >> /etc/bash.bashrc
echo 'export PATH=$PATH:$JAVA_HOME/bin' >> /etc/bash.bashrc

source /etc/bash.bashrc

# alternatives --install /usr/bin/java java usr/local/java/bin/java 2

# alternatives --install /usr/bin/javac javac usr/local/java/bin/javac 2

# alternatives --install /usr/bin/jar jar usr/local/java/bin/jar 2

# alternatives --set java usr/local/java/bin/java

# alternatives --set javac usr/local/java/bin/javac

# alternatives --set jar usr/local/java/bin/jar

#cd /usr/local

cd ..


#wget http://www.eu.apache.org/dist/hadoop/common/hadoop-2.7.2/hadoop-2.7.2.tar.gz
#tar xzf hadoop-2.7.2.tar.gz
#mv hadoop-2.7.2 hadoop/

#echo 'export HADOOP_HOME=/usr/local/hadoop' >> /etc/bash.bashrc
#echo 'export PATH=$PATH:/usr/local/hadoop/bin/' >> /etc/bash.bashrc
#echo 'export HADOOP_HOME=/usr/local/hadoop' >> /etc/bash.bashrc
#echo 'export HADOOP_MAPRED_HOME=$HADOOP_HOME' >> /etc/bash.bashrc
#echo 'export HADOOP_COMMON_HOME=$HADOOP_HOME' >> /etc/bash.bashrc
#echo 'export HADOOP_HDFS_HOME=$HADOOP_HOME' >> /etc/bash.bashrc
#echo 'export YARN_HOME=$HADOOP_HOME' >> /etc/bash.bashrc
#echo 'export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native' >> /etc/bash.bashrc
#echo 'export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin' >> /etc/bash.bashrc
#echo 'export HADOOP_INSTALL=$HADOOP_HOME' >> /etc/bash.bashrc

#source /etc/bash.bashrc

cd /home/vagrant


# Instala MongoDB

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927

echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

sudo apt-get update

sudo apt-get install -y mongodb-org


#instalar mosquitto
# debe ser automatico si no lo deja carpeta
wget http://mosquitto.org/files/source/mosquitto-1.4.8.tar.gz
tar xzf mosquitto-1.4.8.tar.gz

sudo apt-get install apt-file
#apt-file update
#apt-file search uuid/uuid.h


sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
sudo apt-get update
sudo apt-get install mosquitto mosquitto-clients python-mosquitto

#/home/vagrant

#mqqt kafka bridge///    mqqtt bridge mosquitto
wget http://www.us.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz
tar xzf apache-maven-3.3.9-bin.tar.gz
#unzip mqttKafkaBridge-master.zip

#kafka
#wget https://www.apache.org/dyn/closer.cgi?path=/kafka/0.9.0.1/kafka-0.9.0.1-src.tgz
wget http://www-us.apache.org/dist/kafka/0.9.0.1/kafka_2.11-0.9.0.1.tgz
tar xzf kafka_2.11-0.9.0.1.tgz

#spark
wget http://d3kbcqa49mib13.cloudfront.net/spark-1.6.0-bin-hadoop2.6.tgz
tar xzf spark-1.6.0-bin-hadoop2.6.tgz
#Paquetes de node


#service iptables stop
#chkconfig iptables off





