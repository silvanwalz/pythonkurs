from nornir import InitNornir
from nornir.core.task import Result
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
from nornir_netmiko.tasks import netmiko_send_command


'''
##################### Hello World #########################
def hello_world(task):
    return Result(host=task.host, result=f"{task.host.name} existiert!")

nr = InitNornir(config_file='nr-config.yaml')
result = nr.run(task=hello_world)
print_result(result)'''

'''
##################### sho int and mac #########################
nr = InitNornir(config_file='nr-config.yaml')
result = nr.run(task=napalm_get, getters='interfaces')
hosts = nr.inventory.hosts.keys()
for host in hosts:
    print(f"Interfaces of host {host}")
    for interface_name, values in result[host].result['interfaces'].items():
        print(f"Interface: {interface_name}, MAC-Address: {values['mac_address']}")'''


nr = InitNornir(config_file="nr-config.yaml")
result = nr.run(task=netmiko_send_command, command_string="show ip ospf neighbor")
print_result(result)