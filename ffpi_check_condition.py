#!/usr/bin/env python
import RPi.GPIO as GPIO

# Setup for the relais-board
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


# This is the condition from original uC-fancontrol
"""
if (
  ((haIn-haOut) >= values.min_ha_diff) &&
  (rhIn > values.min_rh) &&
  (tempIn > values.min_temp) &&
  (tempIn >= (tempOut - values.deltaTD))
"""
