import paho.mqtt.client as mqtt
import json, time, random

broker = "localhost"
topic = "evc/evc1"

client = mqtt.Client()
client.connect(broker, 1883, 60)

while True:
    payload = {
    "temp_C": round(random.uniform(25, 35), 2),
    "pressure_bar": round(random.uniform(1.0, 2.0), 2),
    "flow_Lmin": round(random.uniform(40, 70), 2)
    }
    client.publish(topic, json.dumps(payload))
    print("Published:", payload)
    time.sleep(10)
    
