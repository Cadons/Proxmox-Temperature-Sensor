import api.sensor as s

import json
import psutil

class TemperatureSensor(s.Sensor):

    __fanON=False
    def __init__(self, id: str, name: str):
        super().__init__(id, name, "temperature_watcher")
        super().notifyServer([],self.config.get_configuration_value("temperature_watcher","stop_cooler_webhook_url"))#reset fan
        self.__fanON=False

       

    def get_value(self) -> json:
        
        return json.dumps(psutil.sensors_temperatures())
    
    def __str__(self):
        return f"TemperatureSensor(id={self.id}, name={self.name})"
   
    def notifyServer(self)->bool:
        avarage_temperature=0
        data=self.get_value()
        data=json.loads(data)
        if(len(data)>0):
            acpitz_temp = float(data['acpitz'][0][1])
            coretemp_temp = float(data['coretemp'][0][1])
            nvme_temp = float(data['nvme'][0][1])
            avarage_temperature=float((acpitz_temp+coretemp_temp+nvme_temp)/3)
            data={"id":self.get_id(), "name":self.get_name(), "value":avarage_temperature}
            if self.onApi == True:
                if avarage_temperature > self.config.get_configuration_value("temperature_watcher","critical_temperature"):
                    super().notifyServer(data,self.config.get_configuration_value("temperature_watcher","alert_webhook_url"))
                    self.__fanON=True
                else:
                    if self.__fanON == True:
                        super().notifyServer(data,self.config.get_configuration_value("temperature_watcher","stop_cooler_webhook_url"))
                        self.__fanON=False
                                  
        if self.onInflux == True:
            #self.loadInfluxDB("temperature",-1)
            self.loadInfluxDB("temperature",avarage_temperature)
       


        
    
