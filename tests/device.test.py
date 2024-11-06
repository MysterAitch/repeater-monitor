import unittest
import os
from models.device import Device


class TestDevice(unittest.TestCase):
    def setUp(self):
        self.test_device = Device("192.168.1.1", "Test Device", "Model X", 10, "TestHost")

    def test_creation(self):
        self.assertIsInstance(self.test_device, Device)
        self.assertEqual(self.test_device.ip_address, "192.168.1.1")
        self.assertEqual(self.test_device.description, "Test Device")
        self.assertEqual(self.test_device.model, "Model X")
        self.assertEqual(self.test_device.zabbix_host_id, 10)
        self.assertEqual(self.test_device.zabbix_host_name, "TestHost")

    def test_repr(self):
        self.assertEqual(
            repr(self.test_device),
            "Device(ip_address='192.168.1.1', description='Test Device', model='Model X', zabbix_host_id=10, zabbix_host_name='TestHost')"
        )

    def test_to_dict(self):
        expected_dict = {
            'ip_address': '192.168.1.1',
            'description': 'Test Device',
            'model': 'Model X',
            'zabbix_host_id': 10,
            'zabbix_host_name': 'TestHost'
        }
        self.assertEqual(self.test_device.to_dict(), expected_dict)

    # devices-test-valid_device_data.json: Contains valid JSON with correctly structured device data.
    def test_load_from_json(self):
        try:
            devices = Device.load_devices_from_json(os.path.join(os.path.dirname(__file__), "devices-test-valid_device_data.json"))
            self.assertIsInstance(devices, list)
            self.assertEqual(len(devices), 3)

            # Check the first device
            self.assertEqual(devices[0].ip_address, "192.168.1.1")
            self.assertEqual(devices[0].description, "Test Device 1")
            self.assertEqual(devices[0].model, "Model X")
            self.assertEqual(devices[0].zabbix_host_id, 10)
            self.assertEqual(devices[0].zabbix_host_name, "TestHost 1")

            # Check the second device
            self.assertEqual(devices[1].ip_address, "192.168.1.2")
            self.assertEqual(devices[1].description, "Test Device 2")
            self.assertEqual(devices[1].model, "Model X")
            self.assertEqual(devices[1].zabbix_host_id, 11)
            self.assertEqual(devices[1].zabbix_host_name, "TestHost 2")

            # Check the third device
            self.assertEqual(devices[2].ip_address, "192.168.1.3")
            self.assertEqual(devices[2].description, "Test Device 3")
            self.assertEqual(devices[2].model, "Model Y")
            self.assertEqual(devices[2].zabbix_host_id, 12)
            self.assertEqual(devices[2].zabbix_host_name, "TestHost 3")

        except Exception as e:
            self.fail(f"load_devices_from_json raised Exception unexpectedly: {e}")

    # devices-test-invalid_file_404.json: Should not exist/not be found
    def test_load_from_json_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            Device.load_devices_from_json(os.path.join(os.path.dirname(__file__), "devices-test-invalid_file_404.json"))

    # devices-test-invalid_json_structure.json: Contains syntactically incorrect JSON to test JSON decoding errors.
    def test_load_from_json_invalid_json(self):
        with self.assertRaises(ValueError):
            Device.load_devices_from_json(os.path.join(os.path.dirname(__file__), "devices-test-invalid_json_structure.json"))

    # devices-test-invalid_device_data.json: Contains valid JSON format but incorrect data schema to test data validation.
    def test_load_from_json_invalid_device_data(self):
        with self.assertRaises(ValueError):
            Device.load_devices_from_json(os.path.join(os.path.dirname(__file__), "devices-test-invalid_device_data.json"))


if __name__ == '__main__':
    unittest.main()
