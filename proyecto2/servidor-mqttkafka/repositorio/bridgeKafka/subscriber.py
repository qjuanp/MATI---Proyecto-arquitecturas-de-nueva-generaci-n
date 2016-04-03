import paho.mqtt.client as mqtt
import ssl
from kafka import KafkaProducer

def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("temperature")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send(msg.topic,msg.payload)

client = mqtt.Client()
client.tls_set("/etc/ssl/certs/mascotsens.pem", certfile="dispositivo1.crt", keyfile="dispositivo1.key", tls_version=ssl.PROTOCOL_TLSv1)
client.on_connect = on_connect
client.on_message = on_message
client.connect("mascotqueue.mascotsens.co",1883, 60)

client.loop_forever()
