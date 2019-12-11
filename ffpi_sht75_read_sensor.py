#!/usr/bin/env python

import math
import time
from sht_sensor import Sht

# Config the pins where the SHT75 are connected
# Sht(clockpin, datapin)
sht_outdoor = Sht(11, 2)
sht_indoor = Sht(11, 3)

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