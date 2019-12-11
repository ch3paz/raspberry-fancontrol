#!/usr/bin/env python

from influxdb import InfluxDBClient
from ffpi_sht75_read_sensor import sht75_read_sensors
from ffpi_check_condition import check_condition

client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('fancontrol')

data_json = sht75_read_sensors()

client.write_points(check_condition(data_json))
