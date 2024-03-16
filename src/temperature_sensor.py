import api.sensor as s

import json
import psutil

class TemperatureSensor(s.Sensor):
    id = None
    name = None
    
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

    def get_value(self) -> json:
        
        return json.dumps(psutil.sensors_temperatures())
    
    def get_name(self) -> str:
        return self.name
    
    def get_id(self) -> str:
        return self.id
    
    def __str__(self):
        return f"TemperatureSensor(id={self.id}, name={self.name})"
    
    def notifyServer(self)->bool:
        data={"id":self.get_id(), "name":self.get_name(), "value":self.get_value()}
        super().notifyServer(data)
        
    
