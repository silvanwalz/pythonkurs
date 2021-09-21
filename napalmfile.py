import napalm

def main():
    hosts = [49, 50, 51, 52, 53, 54, 55, 56]
    counter = 49
    while counter < 56:
        counter = counter + 1
        ip = f'10.18.10.{counter}'
        driver = napalm.get_network_driver('ios')
        device_info = {
            'hostname': ip,
            'username': 'cisco',
            'password': 'cisco'}

        with driver(**device_info) as device:
            for host in hosts:
                if counter != host:
                    print(ip, device.ping(f'10.18.10.{host}'))



'''
        config = 'hostname R50'

        device.load_merge_candidate(config=config)
        print('\nDiff:')
        print(device.compare_config())
        choice = input("\nCommit? [yN]: ")
        if choice == 'y':
            print('Commiting')
            device.commit_config()
        else:
            print('Discarding ...')
            device.discard_config()
'''


if __name__ == '__main__':
    main()