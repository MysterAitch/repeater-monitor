import json
import os


class Device:
    def __init__(self, ip_address, description, model, zabbix_host_id=None, zabbix_host_name=None):
        self.ip_address = ip_address
        self.description = description
        self.model = model
        self.zabbix_host_id = zabbix_host_id
        self.zabbix_host_name = zabbix_host_name

    def __repr__(self):
        return (
            f"Device("
            f"ip_address='{self.ip_address}'"
            f", description='{self.description}'"
            f", model='{self.model}'"
            f", zabbix_host_id={self.zabbix_host_id}"
            f", zabbix_host_name='{self.zabbix_host_name}'"
            f")"
        )

    def to_dict(self):
        return {
            'ip_address': self.ip_address,
            'description': self.description,
            'model': self.model,
            'zabbix_host_id': self.zabbix_host_id,
            'zabbix_host_name': self.zabbix_host_name
        }

    @classmethod
    def load_devices_from_json(cls, file_path: str):
        canonical_path = os.path.realpath(file_path)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} (canonical path: {canonical_path}) does not exist.")

        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            raise ValueError(f"The file {file_path} (canonical path: {canonical_path}) is not a valid JSON file.")
        except Exception as e:
            raise IOError(f"Error reading {file_path} (canonical path: {canonical_path}): {e}")

        devices = []
        for device_data in data:
            try:
                devices.append(Device(**device_data))
            except TypeError as e:
                raise ValueError(f"Error creating Device object from data {device_data}: {e}")

        return devices
