import api.sensor as s

import json
import psutil

class TemperatureSensor(s.Sensor):


    def __init__(self, id: str, name: str):
        super().__init__(id, name, "temperature_watcher")
       

    def get_value(self) -> json:
        
        return json.dumps(psutil.sensors_temperatures())
    
    def __str__(self):
        return f"TemperatureSensor(id={self.id}, name={self.name})"
   
    def notifyServer(self)->bool:
        avarage_temperature=0
        data=self.get_value()
        data=json.loads(data)
        if(len(data)>0):
            acpitz_temp = data['acpitz'][0][1]
            coretemp_temp = data['coretemp'][0][1]
            nvme_temp = data['nvme'][0][1]
            avarage_temperature=(acpitz_temp+coretemp_temp+nvme_temp)/3
            data={"id":self.get_id(), "name":self.get_name(), "value":avarage_temperature}
            if self.onApi == True:
                super().notifyServer(data)
        if self.onInflux == True:
            #self.loadInfluxDB("temperature",-1)
            self.loadInfluxDB("temperature",avarage_temperature)
       


        
    
