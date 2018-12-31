#!/usr/bin/env python3
import Adafruit_BMP.BMP085 as BMP085


if __name__ == '__main__':

    sensor = BMP085.BMP085()
    temperature = sensor.read_temperature()
    pressure = sensor.read_pressure() / 100
    sealevel_pressure =  sensor.read_sealevel_pressure() / 100
    altitude = sensor.read_altitude()

    sid = 'rpi3'
    sensor_type = 'bmp085'

    tags = {'sid' : sid, 'sensor_type': sensor_type}

    #json_body = []

    #json_body.append(meas('sensor', 'temperature', temperature, ctime, tags))
    #json_body.append(meas('sensor', 'pressure', pressure, ctime, tags))
    #json_body.append(meas('sensor', 'sealevel_pressure', sealevel_pressure, ctime, tags))
    #json_body.append(meas('sensor', 'altitude', altitude, ctime, tags))

    print("sensor,sid={},sensor_type={} temperature={}".format(sid, sensor_type, temperature))
    print("sensor,sid={},sensor_type={} pressure={}".format(sid, sensor_type, pressure))
    print("sensor,sid={},sensor_type={} sealevel_pressure={}".format(sid, sensor_type, sealevel_pressure))
    print("sensor,sid={},sensor_type={} altitude={}".format(sid, sensor_type, altitude))

