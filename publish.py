import time
import paho.mqtt.client as paho
from paho import mqtt
from time import sleep
# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNECTED %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("SEND: " + str(mid))



# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("Asem123", "12345678")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("cb067f8850e54fc8ad3051e47899ff31.s2.eu.hivemq.cloud", 8883)

# setting callbacks, use separate functions like above for better visibility

client.on_message = on_message
client.on_publish = on_publish

client.loop_start()

with open('data.json', 'r') as file:
    diagnostic_data = file.read()

# a single publish, this can also be done in loops, etc.
client.publish("Customer", payload=diagnostic_data, qos=2)

client.loop_stop()