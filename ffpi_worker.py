#!/usr/bin/env python

import configparser
from influxdb import InfluxDBClient
from ffpi_sht75_read_sensor import sht75_read_sensors
from ffpi_check_condition import check_condition

# Read settings from file
ffpi_configparser = configparser.RawConfigParser()
ffpi_configfilepath = r'ffpi_settings.config'
ffpi_configparser.read(ffpi_configfilepath)

dbhostname = ffpi_configparser.get('ffpi_influxdb_settings', 'dbhostname')
dbport = ffpi_configparser.get('ffpi_influxdb_settings', 'dbport')
dbname = ffpi_configparser.get('ffpi_influxdb_settings', 'dbname')

client = InfluxDBClient(host=dbhostname, port=dbport)
client.switch_database(dbname)

data_json = sht75_read_sensors()

client.write_points(check_condition(data_json))
