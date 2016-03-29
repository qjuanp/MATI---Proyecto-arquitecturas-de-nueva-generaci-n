import pyspark_cassandra
import pyspark_cassandra.streaming

from pyspark_cassandra import CassandraSparkContext

from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from uuid import uuid1

import json

sc = CassandraSparkContext(conf=conf)
sql = SQLContext(sc)
stream = StreamingContext(sc, 1) # 1 second window

kafka_stream = KafkaUtils.createStream(stream, \
                                       "localhost:2181", \
                                       "raw-event-streaming-consumer",
                                        {"pageviews":1})