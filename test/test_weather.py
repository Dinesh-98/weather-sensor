from influxdb import InfluxDBClient
import sys
sys.path.insert(1,'../weather-sensor')
import app

#Unittesting influxdb connection
def test_influxdb_connection():
    cli = InfluxDBClient('host',8086,'username','password','db')
    assert 'http://host:8086' == cli._baseurl
    assert 'username' == cli._username
    assert 'password' == cli._password
    assert 'db' == cli._database

    cli.switch_database('another_db')
    assert 'another_db' == cli._database

#Unittesting weather details without time duration
def test_get_sensor_details_without_duration():
    sensor_name = "1"
    metric_name = "humidity"
    statistics = "max"
    result = {"output":[{"max":175,"time":"2022-03-28T07:00:00Z"}]}
    assert app.get_sensor_details_without_duration(sensor_name,metric_name,statistics) == (result,200)

#Unittesting weather details with time duration
def test_get_sensor_details():
    sensor_name = "3"
    metric_name = "temperature"
    statistics = "min"
    duration = "1w"
    result = {"output":[{"min":160,"time":"2022-03-27T09:58:00Z"}]}
    assert app.get_sensor_details(sensor_name,metric_name,statistics,duration) == (result,200)