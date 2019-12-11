#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

# Setup for the relais-board
from importlib_metadata.tests import data

Relay_Ch1 = 26
Relay_Ch2 = 20
Relay_Ch3 = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Relay_Ch1, GPIO.OUT)
GPIO.setup(Relay_Ch2, GPIO.OUT)
GPIO.setup(Relay_Ch3, GPIO.OUT)

# Predefined minimums
#
# ahdiff = a minimum difference of AHin-AHout should be (in g/m³)
# rhmin = the minimum humidity we would like to have (relative humidity in %)
# tmin = the minimum temperature we would like to have (in degrees C)

ahdiff = 0.5
rhmin = 65
tmin = 14


def check_condition(data_json):
    for i in data_json:
        data_dict = i.get("fields")

    rhin = float(data_dict.get("RHin"))
    tin = float(data_dict.get("Tin"))
    ahin = float(data_dict.get("AHin"))
    ahout = float(data_dict.get("AHout"))

    if ((ahin - ahout) >= ahdiff) and (rhin > rhmin) and (tin > tmin):
        # Fan ON (Relais CH1 ON)
        GPIO.output(Relay_Ch1, GPIO.LOW)
        data_dict["Fan"] = 1
    else:
        # Fan OFF (Relais CH1 OFF)
        GPIO.output(Relay_Ch1, GPIO.HIGH)
        data_dict["Fan"] = 0

    print(data_dict)
    updated_json = [{
        "measurement": "Datacollect",
        "tags": {
            "Location": "Cellar",
        },
        "time": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "fields": {
            "RHin": data_dict.get("RHin"),
            "RHout": data_dict.get("RHout"),
            "Tin": data_dict.get("Tin"),
            "Tout": data_dict.get("Tout"),
            "DPin": data_dict.get("DPin"),
            "DPout": data_dict.get("DPout"),
            "AHin": data_dict.get("AHin"),
            "AHout": data_dict.get("AHout"),
            "Fan": data_dict.get("Fan")
        }
    }]

    print(updated_json)

    return updated_json
