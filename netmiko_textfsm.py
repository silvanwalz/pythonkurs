from netmiko import Netmiko

device = {
    'host': '10.18.10.50',
    'username': 'cisco',
    'password': 'cisco',
    'device_type': 'cisco_ios'}

net_connect = Netmiko(**device)
#output = net_connect.send_command("show ip int brief")

net_connect.enable()
if net_connect.check_enable_mode():
    #cfg_command = ['hostname R50']
    #cfg_command = ['interface loopback 0', 'ip address 10.10.99.50 255.255.255.0']
    cfg_command = ['router bgp 10', 'neighbor 10.18.10.56 remote-as 6']

    output = net_connect.send_config_set(cfg_command)

print(output)
net_connect.disconnect()



