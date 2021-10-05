import zmq
import napalm_logs.utils
from netmiko import Netmiko

def noshutport(hostname, interface):
    device = {
        'host': hostname,
        'username': 'ins',
        'password': 'ins@lab',
        'device_type': 'cisco_ios'}

    net_connect = Netmiko(**device)
    net_connect.enable()
    if net_connect.check_enable_mode():
        cfg_command = ['conf t', f'interface {interface}', 'no shut', 'end']
        output = net_connect.send_config_set(cfg_command)
    net_connect.disconnect()

def socket_messages():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect('tcp://10.18.10.62:49017')
    socket.setsockopt(zmq.SUBSCRIBE, b'')

    while True:
        raw_object = socket.recv()
        yield napalm_logs.utils.unserialize(raw_object)

for message in socket_messages():
    if message['ip'] == '10.18.10.25':
        if message['error'] == 'INTERFACE_DOWN':
            for key in message['yang_message']['interfaces']['interface']:
                noshutport(message['ip'], key)
