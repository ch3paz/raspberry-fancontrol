#!/usr/bin/env python

import math
import time
import configparser
from sht_sensor import Sht

# Read settings from file
ffpi_configparser = configparser.RawConfigParser()
ffpi_configfilepath = r'ffpi_settings.config'
ffpi_configparser.read(ffpi_configfilepath)

sht_sensor_clock = ffpi_configparser.get('ffpi_sht75_settings', 'sht_sensor_clock')
sht_sensor_1_data = ffpi_configparser.get('ffpi_sht75_settings', 'sht_sensor_1_data')
sht_sensor_2_data = ffpi_configparser.get('ffpi_sht75_settings', 'sht_sensor_2_data')

# Config the pins where the SHT75 are connected
# Sht(clockpin, datapin)
sht_outdoor = Sht(sht_sensor_clock, sht_sensor_1_data)
sht_indoor = Sht(sht_sensor_clock, sht_sensor_2_data)

# Fan ON = 1, OFF =0, UNDEFINED = 2
fanstatus = 2


def sht75_read_sensors():
    # Read indoor sensor
    sht_temperature = sht_indoor.read_t()
    sht_humidity = sht_indoor.read_rh()
    sht_dewpoint = sht_indoor.read_dew_point()
    sht_absolute = 216.7 * (sht_humidity / 100.0 * 6.112 *
                            math.exp(17.62 * sht_temperature /
                                     (243.12 + sht_temperature)) /
                            (273.15 + sht_temperature))

    hval_indoor = format(sht_humidity, "2.1f")
    tval_indoor = format(sht_temperature, "2.1f")
    dval_indoor = format(sht_dewpoint, "2.1f")
    aval_indoor = format(sht_absolute, "2.1f")

    # Read outdoor sensor
    sht_temperature = sht_outdoor.read_t()
    sht_humidity = sht_outdoor.read_rh()
    sht_dewpoint = sht_outdoor.read_dew_point()
    sht_absolute = 216.7 * (sht_humidity / 100.0 * 6.112 *
                            math.exp(17.62 * sht_temperature /
                                     (243.12 + sht_temperature)) /
                            (273.15 + sht_temperature))

    hval_outdoor = format(sht_humidity, "2.1f")
    tval_outdoor = format(sht_temperature, "2.1f")
    dval_outdoor = format(sht_dewpoint, "2.1f")
    aval_outdoor = format(sht_absolute, "2.1f")

    # Json for pushing to influxdb
    data_json = [{
        "measurement": "Datacollect",
        "tags": {
            "Location": "Cellar",
        },
        "time": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "fields": {
            "RHin": hval_indoor,
            "RHout": hval_outdoor,
            "Tin": tval_indoor,
            "Tout": tval_outdoor,
            "DPin": dval_indoor,
            "DPout": dval_outdoor,
            "AHin": aval_indoor,
            "AHout": aval_outdoor,
            "Fan": fanstatus
        }
    }]

    return data_json
