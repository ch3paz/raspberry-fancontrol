#!/usr/bin/env python

import math
import time
from sht_sensor import Sht

sht_outdoor = Sht(11, 2)
sht_indoor = Sht(11, 3)


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

    data_json = [{"Time": time.strftime("%Y-%m-%dT%H:%M:%S"),
                  "RHin": hval_indoor, "RHout": hval_outdoor,
                  "Tin": tval_indoor, "Tout": tval_outdoor,
                  "DPin": dval_indoor, "DPout": dval_outdoor,
                  "AHin": aval_indoor, "AHout": aval_outdoor}]

#    current_datetime = time.strftime("%Y-%m-%dT%H:%M:%S")
#    data_dict.update(Time=current_datetime)
#    data_json = json.dumps(data_dict)

#    print(data_json)
    return data_json

# sht75_read_sensors()
