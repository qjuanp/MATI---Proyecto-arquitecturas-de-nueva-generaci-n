#!/usr/bin/env bash
#~/spark-1.6.0-bin-hadoop2.6/bin/spark-submit --packages org.apache.spark:spark-streaming-kafka_2.10:1.6.1 --py-files /home/arquitectura/mongo-hadoop/spark/src/main/python/pymongo_spark.py,/home/arquitectura/mongo-hadoop/spark/src/main/python/dist/pymongo_spark-0.1.dev0-py2.7.egg spark.py  
~/spark-1.6.0-bin-hadoop2.6/bin/spark-submit --packages org.apache.spark:spark-streaming-kafka_2.10:1.6.1 --jars mongo-hadoop-spark.jar --driver-class-path mongo-hadoop-spark.jar spark.py  
