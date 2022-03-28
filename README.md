# Weather-sensor
Querying sensor data using Flask (Rest API)

### Weather JSON Data: (Manually created json data)
JSON Data consists of 3 sensor. Each sensor has info of humidity, pressure, temperature
and windspeed for the month of March (Mar 1st - Mar 31st)

### Summary:
Goal is to query various sensors to obtain weather info for a particular time duration

### Tools Used:
Python 3.7.3
Influx 1.8.10 (Used influxdb as it's a time series database)
pip 18.1

### Installing InfluxDB: (for Linux)
You can install influxdb in your local from : [HERE](https://devopslifecycle.com/lessons/16/getting-started-with-influxdb#measurement-command-cheat-sheet)

### Running Application:
1. Create a virtual environment for the project:
python3 -m venv venv

2. Activate venv:
source venv/bin/activate

3. Install requirements for the project:
pip install -r requirements.txt

4. Post the json data to influxdb:
python influx_set_payload.py

5. Run flask application:
flask run

Your application will be running on http://localhost:5000/

6. Pytest the flask application:
pytest --cov (Gives you a complete test coverage of which statements are tested and which are missed)

### Details:
1. Get weather details without time duration: (provides us latest details)
http://localhost:5000/sensor/sensor-name/metric/metric-name/stat/statistics

2. Get weather details with time duration:
http://localhost:5000/sensor/sensor-name/metric/metric-name/stat/statistics/time/duration

3. sensor-name: specify which sensor you will be querying (1 or 2 or 3) 

4. metric-name: specify which metric you will be using (temperature or pressure or humidity or windspeed) 

5. statistics: specify which statistics you need to query (max or min or sum or any influxdb related stats)

6. duration: Time Intervals used for querying (1d - 1 Day, 1w - 1 Week, 1m - 1 Month)