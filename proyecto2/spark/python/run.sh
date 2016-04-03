#!/usr/bin/env bash
#~/spark-1.6.0-bin-hadoop2.6/bin/spark-submit --packages org.apache.spark:spark-streaming-kafka_2.10:1.6.1 --py-files /home/arquitectura/mongo-hadoop/spark/src/main/python/pymongo_spark.py,/home/arquitectura/mongo-hadoop/spark/src/main/python/dist/pymongo_spark-0.1.dev0-py2.7.egg spark.py  
~/spark-1.6.0-bin-hadoop2.6/bin/spark-submit --py-files ./pymongo_spark.py --packages org.apache.spark:spark-streaming-kafka_2.10:1.6.1 --driver-class-path="/home/arquitectura/spark-1.6.0-bin-hadoop2.6/lib/mongo-hadoop-spark-1.5.2.jar" spark.py  
