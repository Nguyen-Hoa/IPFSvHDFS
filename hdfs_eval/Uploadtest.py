peers = [
    'http://gimbap.mocalab.org:3000/api/',
    'http://kimchi.mocalab.org:3000/api/',
    'http://kraken.mocalab.org:3000/api/',
    'http://medusa.mocalab.org:3000/api/'
]

key = input()
while key != 'q':
    key = input()
    if key == 'b':
        # Start remote measurements
        for ip in peers:
            response = requests.post(ip+'watts-up-meter-start')
            if response.status_code != 200:
                print(f'Failed to start meter at {ip}')
                exit()

    elif key == 'e':
        # Close remote measurements
        for ip in peers:
            response = requests.post(ip+'watts-up-meter-end')
            if response.status_code != 200:
                print(f'Failed to start meter at {ip}')
                exit()