import  datetime
import os
from sensor import Sensor

#get the date in YYYY-MM-DD format to use in the filename
todaydate = datetime.datetime.now().date().strftime("%Y-%m-%d")

#filepath to store sensor readings in a text file with the current date in the filename
filepath = os.path.join(os.getcwd(), "Sensor_logs", f"Sensor_readings_{todaydate}.txt")

#create sensor objects and log readings
sensor6 = Sensor("Distance", 10)
sensor6.log_reading()
sensor6.log_reading()
sensor6.log_reading()
sensor6.log_reading()

sensor7 = Sensor("Light", 100)
sensor7.log_reading()
sensor7.log_reading()
sensor7.log_reading()
sensor6.log_reading()

#convert each history list to string format
logs_list6 = ','.join(str(reading) for reading in sensor6.history)
logs_list7 = ','.join(str(reading) for reading in sensor7.history)

#write sensor readings to text file
if os.path.exists(filepath):
    with open(filepath, "a") as f:
        f.write(f"sensor6 {sensor6.name} readings: {logs_list6}\n")
        f.write(f"sensor7 {sensor7.name} readings: {logs_list7}\n")
        
else:
    with open(filepath, "w") as f:
        f.write(f"sensor6 {sensor6.name} readings: {logs_list6}\n")
        f.write(f"sensor7 {sensor7.name} readings: {logs_list7}\n") 


