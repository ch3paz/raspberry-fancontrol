# fancy-fanpi

Successor of the "Fancontrol" which was based on an Atmel Mega32, but now for raspberry pi.

# Description

* Controls fans depending on absolute humidity and temperatures
* Influxdb, used for storing gathered measurements 
* Grafana, used for visualisation

## Ideas

* As this should be running independently everything is set up on the pi here

## Pins/Ports/Wiring

TBD

# Prerequisites

## Configure system

Some of my config-files (and location) could be found in this repository for easy copy&paste:

> ./sysconfig_files/

## Install sht-sensor

We do this global:

~~~
sudo pip3 install sht-sensor
~~~

## Install and configure influxdb

As we gather a set of timeseries data (to display it later in grafana) we set up an influxdb.

~~~
sudo apt install apt-transport-https
curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
lsb_release -a
# Depending on output of lsb_release:
echo "deb https://repos.influxdata.com/debian buster stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
sudo apt update
sudo apt-get install influxdb
# Disable reporting, enable IP and port
sudo vim /etc/influxdb/influxdb.conf
sudo systemctl restart influxdb.service
# Create a database
influx
  CREATE DATABASE <db-name>
~~~

## Install and configure grafana

For visualise the gathered data we set up grafana:

TBD
