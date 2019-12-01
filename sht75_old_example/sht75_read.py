#!/usr/bin/env python

import math

from sht1x.Sht1x import Sht1x

dataPin   = 15
clkPin    = 13
sht1x     = Sht1x(dataPin, clkPin, Sht1x.GPIO_BOARD)


def sht75_read():
    # Read the SHT, calc absolute humidity
    SHTtemperature = sht1x.read_temperature_C()
    SHThumidity    = sht1x.read_humidity()
    SHTdewPoint    = sht1x.calculate_dew_point(SHTtemperature, SHThumidity)
    SHTabsolute    = 216.7*(SHThumidity/100.0*6.112*\
                     math.exp(17.62*SHTtemperature/\
                     (243.12+SHTtemperature))/\
                     (273.15+SHTtemperature))
    # Formatting things
    hval = format(SHThumidity, "2.1f")
    tval = format(SHTtemperature, "2.1f")
    dval = format(SHTdewPoint, "2.1f")
    aval = format(SHTabsolute, "2.1f")

    csvList = {"RH": hval, "T": tval, "DP": dval, "AH": aval}
    return csvList
