from flask import Flask
from influxdb import InfluxDBClient
from dateutil.relativedelta import relativedelta
import time, datetime

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to Weather Database. Query to get temperature, humidity, windspeed and pressure"

@app.route("/sensor/<sensor_name>/metric/<metric_name>/stat/<statistics>")
def get_sensor_details_without_duration(sensor_name,metric_name,statistics):
    try:
        current_time = str(int(time.mktime(datetime.datetime.now().timetuple())))
        current_timestamp = current_time.ljust(19,'0') #calculating current epoch timestamp

        lastdaytime = datetime.datetime.now() + datetime.timedelta(days = 1)
        timestamp = str(int(time.mktime(lastdaytime.timetuple())))
        timestamp = timestamp.ljust(19,'0') #calculating next day epoch timestamp
        
        client = InfluxDBClient('localhost',8086,'admin','admin')
        client.create_database('weatherdb')
        client.switch_database('weatherdb')

        if sensor_name == "all":
            query_db = "select " + statistics + "(" + metric_name + ")" + " from sensor where time > " + current_timestamp + " and time < " + timestamp
            results = client.query(query_db) #Result set will be obtained for the above query
            output_data = list(results.get_points())
            return {"output": output_data},200
        elif sensor_name == "1" or sensor_name == "2" or sensor_name == "3":
            query_db = "select " + statistics + "(" + metric_name + ")" + " from sensor where sensor=" + sensor_name + " and time > " + current_timestamp + " and time < " + timestamp
            results = client.query(query_db)
            output_data = list(results.get_points())
            return {"output": output_data},200
        else:
            raise TypeError("No data exists in database for the above query")
    except TypeError as e:
        return {"message": str(e)}, 500
    except:
        return {"message": "InfluxDB doesn't exist. Check if hostname,port,username and password specified is valid"},500


@app.route("/sensor/<sensor_name>/metric/<metric_name>/stat/<statistics>/time/<duration>")
def get_sensor_details(sensor_name,metric_name,statistics,duration):
    try:
        current_time = str(int(time.mktime(datetime.datetime.now().timetuple())))
        current_timestamp = current_time.ljust(19,'0')

        client = InfluxDBClient('localhost',8086,'admin','admin')
        client.create_database('weatherdb')
        client.switch_database('weatherdb')

        if duration == "1m":
            lastmonthtime = datetime.datetime.now() - relativedelta(months = 1)
            timestamp = str(int(time.mktime(lastmonthtime.timetuple())))
            timestamp = timestamp.ljust(19,'0') #calculating epoch timestamp for previous month
        elif duration == "1w":
            lastweektime = datetime.datetime.now() - datetime.timedelta(weeks = 1)
            timestamp = str(int(time.mktime(lastweektime.timetuple())))
            timestamp = timestamp.ljust(19,'0') #calculating epoch timestamp for previous week
        elif duration == "1d":
            lastdaytime = datetime.datetime.now() - datetime.timedelta(days = 1)
            timestamp = str(int(time.mktime(lastdaytime.timetuple())))
            timestamp = timestamp.ljust(19,'0') # calculating epoch timestamp for previous day

        if sensor_name == "all":
            query_db = "select " + statistics + "(" + metric_name + ")" + " from sensor where time > " + timestamp + " and time < " + current_timestamp
            results = client.query(query_db)
            output_data = list(results.get_points())
            return {"output": output_data},200
        elif sensor_name == "1" or sensor_name == "2" or sensor_name == "3":
            query_db = "select " + statistics + "(" + metric_name + ")" + " from sensor where sensor=" + sensor_name + " and time > " + timestamp + " and time < " + current_timestamp
            results = client.query(query_db)
            output_data = list(results.get_points())
            return {"output": output_data},200
        else:
            raise TypeError("No data exists in database for the above query")
    except TypeError as e:
        return {"message": str(e)}, 500
    except:
        return {"message": "InfluxDB doesn't exist. Check if hostname,port,username and password specified is valid"},500


if __name__ == '__main__':
    app.run(host="localhost",port=5000,debug=True)