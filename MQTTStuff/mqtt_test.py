import paho.mqtt.client as mqtt
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################

#to start mosquitto go to the mosquitto installation and run "mosquitto -c new.conf -v"
#nescessary cuz I created a custom .conf file and -v for verbose mode

broker_address="localhost"
client = mqtt.Client('test client')
client.connect(broker_address, port=1883)
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
client.subscribe("columbia/lion")
client.publish("columbia/lion","RAWR")
time.sleep(4)
client.loop_stop() #stop the loop

#resources
# http://www.steves-internet-guide.com/into-mqtt-python-client/
# https://mosquitto.org/man/mosquitto-8.html
