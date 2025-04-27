import unittest
from src.data_validation import validate_message

class TestDataValidation(unittest.TestCase):

    def test_valid_message(self):
        message = {
            "device_id": "device123",
            "timestamp": "2025-04-27T12:00:00Z",
            "sensor_reading": 25.5
        }
        self.assertTrue(validate_message(message))

    def test_missing_fields(self):
        message = {
            "device_id": "device123",
            "sensor_reading": 25.5
        }
        self.assertFalse(validate_message(message))

    def test_invalid_sensor_reading(self):
        message = {
            "device_id": "device123",
            "timestamp": "2025-04-27T12:00:00Z",
            "sensor_reading": "invalid_number"
        }
        self.assertFalse(validate_message(message))

if __name__ == "__main__":
    unittest.main()
