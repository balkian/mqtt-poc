import paho.mqtt.client as mqtt
import os

HOST = os.environ.get('MQTT_HOST', 'localhost')

print('Connecting to %s' %HOST)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #
    # QOS: 0) no confirmation; 1) at least once; 2) at most once

    client.subscribe("/gsi/#", qos=2)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client(client_id='mqtt-server', clean_session=False)
client.on_connect = on_connect
client.on_message = on_message

client.connect(HOST, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
