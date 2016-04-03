from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from uuid import uuid1

import json

sc = SparkContext(appName="KafkaStreaming")
stream = StreamingContext(sc, 1) # 1 second window

kafka_stream = KafkaUtils.createStream(stream, \
                                       "172.24.98.29:8080", \
                                       "raw-event-streaming-consumer",
                                        {"temperature":1})
                                        
parsed = kafka_stream.map(lambda (k, v): json.loads(v))

# configuration for output to MongoDB
config["mongo.output.uri"] = "mongodb://localhost:27017/marketdata.fiveminutebars"
outputFormatClassName = "com.mongodb.hadoop.MongoOutputFormat"

def ohlc(grouping):
    key = grouping[0]
    value = grouping[1]
    
    outputDoc = { "id": value["id"],"tmp": value["tmp"], "ts":value["ts"] } 
    return (None, outputDoc)

resultRDD = parsed.map(ohlc)
resultRDD.saveAsNewAPIHadoopFile("file:///placeholder", outputFormatClassName, None, None, None, None, config)