import paho.mqtt.client as mqtt
import ssl
from config import MQTT_BROKER, MQTT_PORT, MQTT_CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT_CA

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

def connect_mqtt():
    client = mqtt.Client(client_id=MQTT_CLIENT_ID)
    client.tls_set(ca_certs=PATH_TO_ROOT_CA,
                   certfile=PATH_TO_CERT,
                   keyfile=PATH_TO_KEY,
                   tls_version=ssl.PROTOCOL_TLSv1_2)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_BROKER, MQTT_PORT)
    return client
