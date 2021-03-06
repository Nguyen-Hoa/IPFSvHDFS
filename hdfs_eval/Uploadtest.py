import requests

peers = [
    'http://gimbap.mocalab.org:3000/api/',
    'http://kimchi.mocalab.org:3000/api/',
    'http://kraken.mocalab.org:3000/api/',
    'http://medusa.mocalab.org:3000/api/'
]

key = input('Enter a "b" to begin, "e" to end, or "q" to quit: ')
while True:
    if key == 'b':
        # Start remote measurements
        print('starting loggers...')
        for ip in peers:
            response = requests.post(ip+'watts-up-meter-start')
            if response.status_code != 200:
                print(f'Failed to start meter at {ip}')
                exit()
        print('started all remote loggers. Enter "e" to end.')

    elif key in ['e', 'q']:
        # Close remote measurements
        print('stopping loggers...')
        for ip in peers:
            response = requests.post(ip+'watts-up-meter-end')
            if response.status_code != 200:
                print(f'Failed to start meter at {ip}')
                exit()
        print('stopped all remote loggers. Enter "q" to quit.')
    key = input()
    
        