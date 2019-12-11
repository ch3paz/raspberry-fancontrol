#!/usr/bin/env python

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
        data_list = i.get("fields")

    rhin = data_list.get("RHin")
    tin = data_list.get("Tin")
    ahin = data_list.get("AHin")
    ahout = data_list.get("AHout")

    if ((ahin-ahout) >= ahdiff) and (rhin > rhmin) and (tin > tmin):
        print("Fan ON")
    else:
        print("Fan OFF")

# This is the condition from original uC-fancontrol
"""
if (
  ((haIn-haOut) >= values.min_ha_diff) &&
  (rhIn > values.min_rh) &&
  (tempIn > values.min_temp) &&
  (tempIn >= (tempOut - values.deltaTD))
"""
