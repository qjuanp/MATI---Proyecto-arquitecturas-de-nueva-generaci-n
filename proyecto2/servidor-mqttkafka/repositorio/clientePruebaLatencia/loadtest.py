#!/usr/bin/python

# Copyright (c) 2014 Roger Light <roger@atchoo.org>
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Distribution License v1.0
# which accompanies this distribution.
#
# The Eclipse Distribution License is available at
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    Roger Light - initial implementation

# This shows an example of using the publish.single helper function.

import sys
import ssl
from random import uniform

def publisher1():
	#print("publicador1")
	#publish.single("temperature", mensaje1, hostname="172.28.128.7")
	return

def publisher2():
    #print("publicador2")
    adic ={'ca_certs':"/etc/ssl/certs/mascotsens.pem",
        'tls_version':ssl.PROTOCOL_TLSv1,
        'certfile':"dispositivo1.crt",
         'keyfile':"dispositivo1.key" }
    publish.single("temperature", mensaje2 , hostname="mascotqueue.mascotsens.co", tls=adic)
    return

try:
    import paho.mqtt.publish as publish
except ImportError:
    # This part is only required to run the example from within the examples
    # directory when the module itself is not installed.
    #
    # If you have the module installed, just use "import paho.mqtt.publish"
    import os
    import inspect
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../src")))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
    import paho.mqtt.publish as publish

import time
import threading

loopsTest = 41
counter = 0
counterRequest = 0
requests = 1
mensaje1 = "Mensaje dispositivo 1"
mensaje2 = "Mensaje dispositivo 2 kafka_"
timeAfter = 0
threads = list()
while (counter < loopsTest):
    print("Time After "+str(timeAfter))
    while (timeAfter > time.time()):
        pass
    timeAfter = time.time() + 1
    #time.sleep(1)
    counterRequest = 0
	#publish.single("temperature", mensaje1, hostname="172.28.128.7")
    counter = counter + 1
    while (counterRequest < requests):
        mensaje2 = "{\"id\":\""+ str(counterRequest)+"\", \"tmp\":"+str((39+(round(uniform(-1,2),2))))+", \"ts\":"+str(round(time.time()*1000))+"}"
        t2 = threading.Thread(target=publisher2)
        threads.append(t2)
        t2.start()
		#publish.single("temperature", mensaje2+" "+str(counter), hostname="172.28.128.7")
        counterRequest = counterRequest + 1
