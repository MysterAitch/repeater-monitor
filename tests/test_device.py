import pytest
import os
from models.device import Device


@pytest.fixture
def test_device():
    return Device("192.168.1.1", "Test Device", "Model X", 10, "TestHost")


def test_creation(test_device):
    assert isinstance(test_device, Device)
    assert test_device.ip_address == "192.168.1.1"
    assert test_device.description == "Test Device"
    assert test_device.model == "Model X"
    assert test_device.zabbix_host_id == 10
    assert test_device.zabbix_host_name == "TestHost"


def test_repr(test_device):
    expected_repr = (
        "Device(ip_address='192.168.1.1', description='Test Device', model='Model X', zabbix_host_id=10, zabbix_host_name='TestHost')"
    )
    assert repr(test_device) == expected_repr


def test_to_dict(test_device):
    expected_dict = {
        'ip_address': '192.168.1.1',
        'description': 'Test Device',
        'model': 'Model X',
        'zabbix_host_id': 10,
        'zabbix_host_name': 'TestHost'
    }
    assert test_device.to_dict() == expected_dict


def test_load_from_json():
    try:
        devices = Device.load_devices_from_json(
            os.path.join(os.path.dirname(__file__), "devices-test-valid_device_data.json"))
        assert isinstance(devices, list)
        assert len(devices) == 3

        assert devices[0].ip_address == "192.168.1.1"
        assert devices[0].description == "Test Device 1"
        assert devices[0].model == "Model X"
        assert devices[0].zabbix_host_id == 10
        assert devices[0].zabbix_host_name == "TestHost 1"

        assert devices[1].ip_address == "192.168.1.2"
        assert devices[1].description == "Test Device 2"
        assert devices[1].model == "Model X"
        assert devices[1].zabbix_host_id == 11
        assert devices[1].zabbix_host_name == "TestHost 2"

        assert devices[2].ip_address == "192.168.1.3"
        assert devices[2].description == "Test Device 3"
        assert devices[2].model == "Model Y"
        assert devices[2].zabbix_host_id == 12
        assert devices[2].zabbix_host_name == "TestHost 3"

    except Exception as e:
        pytest.fail(f"load_devices_from_json raised Exception unexpectedly: {e}")


def test_load_from_json_file_not_found():
    with pytest.raises(FileNotFoundError):
        Device.load_devices_from_json(os.path.join(os.path.dirname(__file__), "devices-test-invalid_file_404.json"))


def test_load_from_json_invalid_json():
    with pytest.raises(ValueError):
        Device.load_devices_from_json(
            os.path.join(os.path.dirname(__file__), "devices-test-invalid_json_structure.json"))


def test_load_from_json_invalid_device_data():
    with pytest.raises(ValueError):
        Device.load_devices_from_json(os.path.join(os.path.dirname(__file__), "devices-test-invalid_device_data.json"))
