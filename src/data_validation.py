def validate_message(message: dict) -> bool:
    required_keys = ["device_id", "timestamp", "sensor_reading"]

    for key in required_keys:
        if key not in message:
            print(f"Validation failed: Missing key {key}")
            return False

    if not isinstance(message["sensor_reading"], (int, float)):
        print("Validation failed: sensor_reading must be a number")
        return False

    return True
