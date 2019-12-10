# fancy-fanpi

Successor of the "Fancontrol" which was based on an Atmel Mega32, but now for raspberry pi.

# Description

* Controls fans depending on absolute humidity and temperatures
* Influxdb, used for storing gathered measurements 
* Grafana, used for visualisation

## More notes, ideas and more descriptive stuff

* Everything is set up on the pi here directly (see below)
    - python modules
    - influxdb
    - grafana
* Security is **ignored by default** in this setup
    - no SSL
    - no users and passwords
    
## Pins/Ports/Wiring

Sensor indoor
  * CLK Pin 23, GPIO 11
  * DATA Pin 5, GPIO 3
  
Sensor outdoor
  * CLK Pin 23, GPIO 11
  * DATA Pin 3 GPIO 2

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
  CREATE DATABASE fancontrol
~~~

## Install and configure grafana

To visualise the gathered data we set up grafana.

~~~
sudo apt-get install -y software-properties-common wget
# Attention: The next package depends on your architecture the pi uses!
cd /tmp && wget https://dl.grafana.com/oss/release/grafana-rpi_6.5.1_armhf.deb
sudo dpkg -i grafana-rpi_6.5.1_armhf.deb
# As the package states, now
sudo /bin/systemctl daemon-reload
sudo /bin/systemctl enable grafana-server
sudo /bin/systemctl start grafana-server
# The server starts up and should be accessible after a while on port 3000.
# First login with admin:admin then.
~~~

After login you have to set up the datasource (influxdb, http://localhost:8086) and create a dashboard.