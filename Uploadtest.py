from time import time, sleep
from meter import Meter, Util
import subprocess
import threading
import datetime as dt
import requests

def get_current_time(start=0, end=-1):
    """
        Returns current time in YYYY-MM-DD_HH:MM format
    """
    now = str(dt.datetime.now())
    now = now.replace(' ', '_')
    now = now[start:end]
    return now
now = get_current_time(start=5, end=-10)

peers = [
    'http://kimchi.mocalab.org:3000/api/',
    'http://kraken.mocalab.org:3000/api/',
    'http://medusa.mocalab.org:3000/api/',
]

# Start remote measurements
for ip in peers:
    response = requests.post(ip+'watts-up-meter-start')
    if response.status_code != 200:
        print(f'Failed to start meter at {ip}')
        return 0

# Start local measurements
power_meter = Meter('ttyUSB0')
power_meter.start(f'./results/{now}.power')

sleep(3)

util_meter = Util('3222588,3223869')
util_meter.start(f'./results/{now}.util')


# Begin pinning
filename = './data/images.tar'
cmd = ['ipfs-cluster-ctl', 'add', '-n', 'tar_dogs', filename]
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

sleep(3)

t0 = time()
output = process.communicate()
t_final = time() - t0

print(output)

# Close local measurement
power_meter.cleanup()
util_meter.cleanup()

# Close remote measurements
for ip in peers:
    response = requests.post(ip+'watts-up-meter-end')
    if response.status_code != 200:
        print(f'Failed to start meter at {ip}')
        return 0

print(f'Pinning <{filename}> took: {t_final} seconds')