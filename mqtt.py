import paho.mqtt.client as paho
import time
broker = "broker.mqttdashboard.com"

def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))

client= paho.Client("client1") 
client.on_message=on_message
print("connecting to broker ",broker)

#connect
client.connect(broker, 1883)
client.loop_start() 

#start loop to process received messages
print("subscribing ")

#subscribe
client.subscribe("house/bulb1")

time.sleep(2)
print("publishing ")
#publish
client.publish("house/bulb1","on")

time.sleep(4)
client.disconnect() 
client.loop_stop()