import paho.mqtt.client as mqtt
import time

broker_address = "test.mosquitto.org"

client = mqtt.Client("CGUI")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connection successful")
    else:
        print("bad connection", rc)

client.on_connect = on_connect

try:
    client.connect(broker_address, port=1883)
    client.loop_start()
    time.sleep(4)
    client.loop_stop()

except Exception as e:
    print("connection failed", e)
    exit(1)




