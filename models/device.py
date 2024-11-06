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
