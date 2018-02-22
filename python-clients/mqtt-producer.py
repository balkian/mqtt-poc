import paho.mqtt.publish as publish
import os
import time
import socket

HOSTNAME = socket.gethostname()

HOST = os.environ.get('MQTT_HOST', 'localhost')

print('Connecting to %s' %HOST)

topic = "/gsi/test/multiple"

i = 0
while True:
    print('%s pushing msg %s' %(HOSTNAME, i))
    publish.single(topic=topic, payload='%s says %s' %(HOSTNAME, i), qos=1, hostname=HOST)
    i += 1
    time.sleep(2)
