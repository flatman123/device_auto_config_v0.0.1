from decrypt_file import decrypt
from get_commands import fetch_commands
import netmiko
import os
import concurrent.futures

hosts = decrypt(f'{os.getcwd()}/device_json.gpg')

def send_commands(connection, host, commands):
    connection.send_config_set(commands)
    return

def run(ip_address):
    for device in hosts:
        device_info = {
            "username": hosts[device][0],
            "port": 22,
            "device_type": hosts[device][-2],
            "host": ip_address,
            "verbose": True,
            "password": hosts[device][1]
        }
    connect = netmiko.ConnectHandler(**device_info)
    commands = fetch_commands(hosts[device][-1])
    send_commands(connect, device_info['host'], commands)
    return

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        host_addresses = [hosts[ip][2] for ip in hosts]
        executor.map(run, host_addresses)



