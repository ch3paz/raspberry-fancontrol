from influxdb import InfluxDBClient
from ffpi_sht75_read_sensor import sht75_read_sensors

client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('fancontrol')
client.write_points([sht75_read_sensors()])
