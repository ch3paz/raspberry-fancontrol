#!/usr/bin/env python

from influxdb import InfluxDBClient
from ffpi_sht75_read_sensor import sht75_read_sensors

client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('fancontrol')

data_json = sht75_read_sensors()
# print(data_json)
client.write_points(data_json)
