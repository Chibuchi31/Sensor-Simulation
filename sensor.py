#Sensor simulation
import random



class Sensor:
    
    field_dictionary = {
        "Temperature": "°C",
        "Humidity": "%",
        "Pressure": "Pa",
        "Voltage": "V",
        "Light": "Lux",
        "Distance": "m"
    }
    
    def __init__(self, name:str, value:float):
        
        #assign to self object
        self.name = name
        self.value = value
        #Empty list to store historical sensor readings
        self.history = []
        
        #validaion for recieved arguments
        assert self.name in self.field_dictionary,f"Unit {self.name} is not a valid field factor. Valid field factor names are {list(self.field_dictionary.keys())}"
        assert self.value >= 0.0, f"Value {self.value} is not greater than or equal to zero!"
        
        #Get the unit for the sensor based on the name argument
        self.unit = self.field_dictionary.get(name)
        
        
    #Generate new value for sensor reading
    def _read_value(self): #single underscore convention for internal use
        self.value = random.uniform(0.0,100.0)
        self.value = round(self.value,2)
        return self.value
    
    
    #Add historical sensor reading to list
    def log_reading(self):
        self._read_value()
        self.history.append(self.value)
  
    #Print sensor reading in human text format
    def print_value(self):
        self.log_reading()
        print(
            f"""---Environment report---
        Field Factor: The {self.name} is {self.value:.2f} {self.unit}""")
    
  
        
sensor1 = Sensor('Humidity', 60)
sensor1.log_reading()
sensor1.log_reading()
sensor1.print_value()
print(sensor1.history)