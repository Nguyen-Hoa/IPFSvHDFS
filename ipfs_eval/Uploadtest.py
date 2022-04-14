from time import time, sleep
from meter import Meter, Util
import subprocess
import threading
import datetime as dt
import requests
from env import pids, peers, target_file

def get_current_time(start=0, end=-1):
    """
        Returns current time in YYYY-MM-DD_HH:MM format
    """
    now = str(dt.datetime.now())
    now = now.replace(' ', '_')
    now = now[start:end]
    return now
now = get_current_time(start=5, end=-10)

# Start remote measurements
for ip in peers:
    response = requests.post(ip+'watts-up-meter-start')
    if response.status_code != 200:
        print(f'Failed to start meter at {ip}')
        exit()

# Start local measurements
power_meter = Meter('ttyUSB0')
power_meter.start(f'./results/{now}.power')
util_meter = Util(pids)
util_meter.start(f'./results/{now}.util')

sleep(3)

# Begin pinning
cmd = ['ipfs-cluster-ctl', 'add', '-n', 'tar_dogs', target_file]
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

t0 = time()
output = process.communicate()
t_final = time() - t0

sleep(3)

print(output)

# Close local measurement
power_meter.cleanup()
util_meter.cleanup()

# Close remote measurements
for ip in peers:
    response = requests.post(ip+'watts-up-meter-end')
    if response.status_code != 200:
        print(f'Failed to start meter at {ip}')
        exit()

print(f'Pinning <{target_file}> took: {t_final} seconds')
