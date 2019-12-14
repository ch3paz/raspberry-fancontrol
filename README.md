# fancy-fanpi

Successor of the [Fancontrol](https://github.com/ch3paz/uC-mega32-fancontrol) 
which was based on an Atmel Mega32, but now for raspberry pi.

# Description

* Controls fans depending on absolute humidity and temperatures
* Influxdb, used for storing gathered measurements 
* Grafana, used for visualisation

## More notes, ideas and more descriptive stuff

* Everything is set up on the pi here directly (see instructions below)
    - python modules
    - influxdb
    - grafana
* Security is **ignored by default** in this setup
    - no SSL
    - no users and passwords
    
## Pins/Ports/Wiring/Settings

See the comments in the file
* ffpi_settings.config

All settings have to be done there.

# Prerequisites

## Configure system

Some of my config-files (and location) could be found in this repository for easy copy&paste:

~~~
sysconfig_files/
└── etc
    ├── influxdb
    │   └── influxdb.conf
    └── systemd
        └── system
            └── fancontrol-timer.service
~~~

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
But first gather some data - else grafana won't print nothing ;)

## Run the pythonscript as timer

To log data every 'n' minutes and check if it's worth to run the fans we'll set up an systemd-timer for the script.
Example-servicefile could be found in the sysconfig_files-folder of this repository. Make shure you adapted the
paths in there to your environment!

~~~
sudo cp sysconfig_files/etc/systemd/system/fancontrol-timer.service /etc/systemd/system/fancontrol-timer.service
sudo cp sysconfig_files/etc/systemd/system/fancontrol-timer.timer /etc/systemd/system/fancontrol-timer.timer
sudo systemctl start fancontrol-timer.timer
sudo systemctl enable fancontrol-timer.timer
~~~
