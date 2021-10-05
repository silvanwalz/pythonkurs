#martin.stypinski@ost.ch
'''import pymsteams

myTeamsMessage = pymsteams.connectorcard('https://ostch.webhook.office.com/webhookb2/c09cc1bb-a21a-4caa-a01b-c792f29928c2@a6e70fa3-1c7a-4aa2-a25e-836eea52ca22/IncomingWebhook/2ba831a5910347338b6bcd6216b25f68/d204fac7-dcfc-4364-a02a-a33b2234b7e3')

myTeamsMessage.text('This is from Silvan!')
myTeamsMessage.send()'''

import requests

start = input('Please enter start:')
end = input('Please enter end:')
maxtransfer = int(input('Please enter max transfers:'))

response = requests.get(f'http://transport.opendata.ch/v1/connections?from={start}&to={end}')
#response = requests.get('http://transport.opendata.ch/v1/connections?from=Rapperswil&to=Winterthur')

for i in range(3):
    if response.json()['connections'][i]['transfers'] <= maxtransfer:
        print('---------------------------------------')
        print(f"departure time: {response.json()['connections'][i]['from']['departure']}")
        print(f"arrival time:   {response.json()['connections'][i]['to']['arrival']}")
        print(f"duration:       {response.json()['connections'][i]['duration']}")

'''
mylist = {'error': 'INTERFACE_DOWN', 'host': 'syslogrouter3', 'ip': '10.18.10.25', 'timestamp': 1632830345, 'yang_message': {'interfaces': {'interface': {'GigabitEthernet2': {'state': {'admin_status': 'DOWN'}}}}}, 'message_details': {'messageId': '146', 'host': 'syslogrouter3', 'date': 'Sep 28', 'time': '11:59:05', 'milliseconds': '519', 'timeZone': None, 'tag': 'LINK-5-CHANGED', 'pri': '189', 'message': 'Interface GigabitEthernet2, changed state to administratively down', 'facility': 23, 'severity': 5}, 'yang_model': 'openconfig-interfaces', 'os': 'ios', 'facility': 23, 'severity': 5}

for key in mylist['yang_message']['interfaces']['interface']:
    print(key)
'''
'''
############## Übung 8 ####################
from jinja2 import Environment, FileSystemLoader
import yaml

def main():
    with open('users.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    env = Environment(loader=FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('template.j2')
    for e in data:
        print(template.render(e))

if __name__ == '__main__':
    main()
'''
'''
############## Übung 7 ####################
import yaml
def main():
    #read yaml
    with open('users.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        print(data)

    #write yaml
    users = [{'name': 'John', 'job': 'gardener'},
             {'name': 'Lucy', 'job': 'teacher'}]

    with open('users.yaml', 'w') as f:
        yaml.dump(users, f, sort_keys=False)

if __name__ == '__main__':
    main()
'''
'''
############## Übung 6 ####################
import json

def main():
    with open('jsondata.txt') as jsonfile:
        data = json.load(jsonfile)
        print(data[0]['city'])

    raw_json = [{'name': 'john',
                'city': 'zurich'},
                {'name': 'tim',
                'city': 'rappi'}
                ]
    with open('jsondata.txt', 'w') as jsonfile:
        json.dump(raw_json, jsonfile)

if __name__ == '__main__':
    main()
'''
'''
############## Übung 5 ####################
import csv

def main():
    fieldnames = ['sn', 'pid', 'ip']
    dict = [{'sn': '101',
            'pid': 'ws01',
            'ip': '1.1.1.1'},
            {'sn': '102',
            'pid': 'ws02',
            'ip': '1.1.1.2'},
            {'sn': '103',
             'pid': 'ws03',
             'ip': '1.1.1.3'}
            ]

    with open('test.csv', 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator='\n', delimiter=';')
        writer.writeheader()
        writer.writerows(dict)


if __name__ == '__main__':
    main()
'''
'''
############## Übung 4 ####################
def main(input):
    if input == input[::-1]:
        print('yes')
    else:
        print('no')

if __name__ == '__main__':
    main('33634')
'''
'''
############## Übung 3 ####################
def main():
    price = 0
    shopping_cart = {'banana': 3,
                    'apple': 5,
                    'milk': 10,
                    'beer': 12
                    }

    prices = {'banana': 0.60,
            'apple': 0.60,
            'milk': 1.70,
            'cola': 1.20,
            'beer': 1.10
            }

    for key in shopping_cart.keys():
        price = price + prices[key] * shopping_cart[key]

    print(price)

if __name__ == '__main__':
    main()
'''
'''
############## Übung 2 ####################
def main():
    data = 'Device1:1.1.1.1:vlan1,Device2:2.2.2.2:vlan2,Device3:3.3.3.3:vlan3'
    newdata = data.split(',')
    for i in newdata:
        print(i.split(':'))

if __name__ == '__main__':
    main()
'''
'''
############## Übung 1 ####################
 def summe(number1, number2):
    counter = 1
    #if number1 + number2 >= 10:
    while counter < 10:
        counter = counter + 1
        print(counter)
        #print('Summe ist gleich oder grösser als 10')
    else:
        print('counter ist bei 10 angelangt')
        #print('Summe ist kleiner als 10')
if __name__ == '__main__':
    summe(4,6)
'''