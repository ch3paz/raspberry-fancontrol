#!/usr/bin/env python

import math

from sht_sensor import Sht

sht_indoor = Sht(11, 2)
sht_outdoor = Sht(11, 3)

print('Temperature', sht_indoor.read_t())
print('Relative Humidity', sht_indoor.read_rh())


def sht75_read_sensor():
    # Read the SHT, calc absolute humidity
    sht_temperature = sht1x.read_temperature_C()
    sht_humidity = sht1x.read_humidity()
    sht_dewpoint = sht1x.calculate_dew_point(sht_temperature, sht_humidity)
    sht_absolute = 216.7 * (sht_humidity / 100.0 * 6.112 *
                            math.exp(17.62 * sht_temperature /
                            (243.12 + sht_temperature)) /
                            (273.15 + sht_temperature))
    # Formatting things
    hval = format(sht_humidity, "2.1f")
    tval = format(sht_temperature, "2.1f")
    dval = format(sht_dewpoint, "2.1f")
    aval = format(sht_absolute, "2.1f")

    csvList = {"RH": hval, "T": tval, "DP": dval, "AH": aval}
    return csvList
