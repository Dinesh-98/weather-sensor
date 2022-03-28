from influxdb import InfluxDBClient
from weather_data import json_payload

#Setup InfluxDBClient
client = InfluxDBClient('localhost',8086,'admin','admin')

#Create Database
client.create_database('weatherdb')

#Switch to created database
client.switch_database('weatherdb')

#Write json object into influxdb
client.write_points(json_payload)