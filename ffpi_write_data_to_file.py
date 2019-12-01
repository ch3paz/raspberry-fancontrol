#!/usr/bin/env python

from ffpi_sht75_read_sensor import *
import time


readDelay = 300    # Delay in seconds


def get_read_delay(self):
    return readDelay


while True:
    currDate = time.strftime("%d/%m/%Y")
    currTime = time.strftime("%H/%M/%S")
    dateDict = {"DATE": currDate, "TIME": currTime}
    try:
        currData = sht75_read_sensor()
    except:
        time.sleep(3)
        currData = sht75_read_sensor()
    currData.update(dateDict)

    try:
        f = open("/home/pi/code/sht75/messwerte/messwerte.csv", "a")
        f.write(str(currData) + "\n")
        f.close()
    except:
        print ("Fileoperation failed...")

    time.sleep(readDelay)
