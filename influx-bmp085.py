#!/usr/bin/env python3
from influxdb import InfluxDBClient
import time
import datetime
import serial

import Adafruit_BMP.BMP085 as BMP085

DATABASE = 'sensor'
HOST = '10.0.0.190'
PORT = 8086

def meas(meas, fields, value, timestamp, tags):
    meas = {
        "measurement": meas,
        "tags": {
            "host": "rpi3",
        },
        "time": timestamp,
        "fields": {
            fields: value
        }
    }
    meas['tags'].update(tags)
    return meas


if __name__ == '__main__':
    client = InfluxDBClient(host=HOST, port=PORT, database=DATABASE)

    while True:
        sensor = BMP085.BMP085()
        temperature = sensor.read_temperature()
        pressure = sensor.read_pressure() / 100
        sealevel_pressure =  sensor.read_sealevel_pressure() / 100
        altitude = sensor.read_altitude()

        ctime = datetime.datetime.utcnow()
        sid = 'rpi3'
        sensor_type = 'bmp085'

        tags = {'sid' : sid, 'sensor_type': sensor_type}

        json_body = []

        json_body.append(meas('sensor', 'temperature', temperature, ctime, tags))
        json_body.append(meas('sensor', 'pressure', pressure, ctime, tags))
        json_body.append(meas('sensor', 'sealevel_pressure', sealevel_pressure, ctime, tags))
        json_body.append(meas('sensor', 'altitude', altitude, ctime, tags))

        client.write_points(json_body)
        time.sleep(10)
