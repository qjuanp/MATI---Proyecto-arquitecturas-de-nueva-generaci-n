from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pymongo import MongoClient

from uuid import uuid1

import json

import pymongo_spark
pymongo_spark.activate()

conf = SparkConf() \
            .setAppName("KafkaStreaming") \
            .set('spark.executor.extraClassPath', '/home/arquitectura/spark-1.6.0-bin-hadoop2.6/lib/mongo-hadoop-spark-1.5.2.jar')

sc = SparkContext(conf=conf)
stream = StreamingContext(sc, 1) # 1 second window

kafka_stream = KafkaUtils.createStream(stream, \
                                       "172.24.98.29:8080", \
                                       "raw-event-streaming-consumer",
                                        {"temperature":1})
                                        
parsed = kafka_stream.map(lambda (k, v): json.loads(v))


def ohlc(grouping):
    key = grouping[0]
    value = grouping[1]
    print key
    print value
    outputDoc = { "id": value["id"],"tmp": value["tmp"], "ts":value["ts"] } 
    return (None, outputDoc)    

resultRDD = parsed.map(ohlc).foreachRDD()



client = MongoClient("mongodb://localhost:3001/meteor")

resultRDD.foreachRDD(lambda (x): client.temperature.insert_one(x))