# MQTT Broker Configuration
MQTT_BROKER = "your-mqtt-broker-endpoint.amazonaws.com"
MQTT_PORT = 8883
MQTT_TOPIC = "iot/devices/data"
MQTT_CLIENT_ID = "IoTDataPipelineClient"

# AWS IoT Core Configuration
AWS_REGION = "your-aws-region"
AWS_IOT_ENDPOINT = "your-iot-endpoint.amazonaws.com"

# Security Certificates (if using AWS IoT certificates)
PATH_TO_CERT = "certs/device-certificate.pem.crt"
PATH_TO_KEY = "certs/private.pem.key"
PATH_TO_ROOT_CA = "certs/AmazonRootCA1.pem"
