import os
from sensor import Sensor

# Directory to store sensor logs
os.makedirs("Sensor_logs", exist_ok=True)

#Sensor object creation and loggind readings
sensor2 = Sensor("Temperature",25.5)
sensor2.log_reading()
sensor2.log_reading()
sensor2.log_reading()
sensor2.log_reading()

#Converting sensor readings from list format to string format to write in text file
logs_list2 = ','.join(str(reading) for reading in sensor2.history)

#Text file in directory to store sensor  readings
sensor_readings_txt_filepath = os.path.join(os.getcwd(), "Sensor_logs", "Sensor_readings.txt")

#Append all log reading to text file
with open(sensor_readings_txt_filepath, "a") as f:
    f.write(f"Sensor 2 Readings: {logs_list2} {sensor2.name}{sensor2.unit}\n")