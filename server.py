#!/usr/lib/python3

# server dependencies
import sys
from flask import Flask, request, jsonify, render_template, Response
from meter import Meter, Util

# get system parameters
import datetime as dt

def get_current_time(start=0, end=-1):
    """
        Returns current time in YYYY-MM-DD_HH:MM format
    """
    now = str(dt.datetime.now())
    now = now.replace(' ', '_')
    now = now[start:end]
    return now


app = Flask(__name__)

power_meter = Meter('ttyUSB0')
util_meter = Util('3222588,3223869')

@app.route('/api/watts-up-meter-start', methods=['POST'])
def start_meter():
    try:
        now = get_current_time(start=5, end=-10)
        power_meter.start(f'./results/{now}.power')
        util_meter.start(f'./results/{now}.util')
        return jsonify(result={'message': 'meters successfully started'}), 200
    except:
        print(sys.exc_info()[0:5])
        return jsonify(error={'message': 'Failed to start power meter'}),500

@app.route('/api/watts-up-meter-end', methods=['POST'])
def end_meter():
    try:
        power_meter.cleanup()
        util_meter.cleanup()
        return jsonify(result={'message': 'meters successfully stopped'}), 200
    except:
        print(sys.exc_info()[0:5])
        return jsonify(error={'message': 'Failed to stop or copy power meter'}), 500
