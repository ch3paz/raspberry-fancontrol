#!/usr/bin/env python

import math

from sht_sensor import Sht

sht_indoor = Sht(11, 2)
sht_outdoor = Sht(11, 3)


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

    csvlist = {"RHin": hval_indoor, "Tin": tval_indoor, "DPin": dval_indoor, "AHin": aval_indoor, "RHout": hval_outdoor,
               "Tout": tval_outdoor, "DPout": dval_outdoor, "AHout": aval_outdoor}

    sht75_read_sensors()
    print(csvlist)
    return csvlist