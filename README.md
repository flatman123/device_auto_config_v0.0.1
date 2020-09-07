# device_auto_config_v0.0.1

This script will decrypt encrypted-json-files that were encrypted using gnupg and will then configure networking devices accordingly. This script can be used to configure devices in a multi-vendor network.

Example of json format:
{
    "d0":["admin","cisco123","192.168.0.154","cisco_ios","DEFAULT_CONFIG_1.cfg"],
    "d1":["admin","cisco123","192.168.0.158","cisco_ios","DEFAULT_CONFIG_2.cfg"],
    "d2":["admin","cisco123","192.168.0.230","cisco_ios","DEFAULT_CONFIG_3.cfg"]
}

NOTE: This script utilizes the python netmiko module, so you will need to look up your device_type via netmiko's docs and adjust your json file accordingly.
