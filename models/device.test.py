import unittest

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


if __name__ == '__main__':
    unittest.main()
