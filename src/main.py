import json
from mqtt_client import connect_mqtt
from data_validation import validate_message
from config import MQTT_TOPIC

def main():
    client = connect_mqtt()

    def custom_on_message(client, userdata, msg):
        try:
            payload = json.loads(msg.payload.decode())
            if validate_message(payload):
                print("Data validated and processed:", payload)
            else:
                print("Invalid data received.")
        except Exception as e:
            print(f"Error processing message: {e}")

    client.on_message = custom_on_message

    client.subscribe(MQTT_TOPIC)
    client.loop_forever()

if __name__ == "__main__":
    main()
