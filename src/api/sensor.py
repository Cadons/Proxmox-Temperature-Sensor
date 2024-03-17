import json
import api.configuration_reader as cr
import requests
from abc import ABC, abstractmethod
class Sensor(ABC):
    id = None
    name = None
    __sensorName=None
    config: cr.ConfigurationReader=cr.ConfigurationReader()
    def __init__(self, id: str, name: str, sensorName:str):
        self.id = id
        self.name = name
        self.__sensorName=sensorName
    
    
    @abstractmethod
    def get_value(self) -> json:
        raise NotImplementedError()

    def get_name(self) -> str:
        return self.name
 
    def get_id(self) -> str:
        return self.id
    
    def notifyServer(self, inputData)->bool:
        url=self.config.get_configuration_value(self.__sensorName,"monitoring_server_url")
        headers = {'Content-Type': 'application/json'}
        data =inputData
        try:
            response = requests.post(url, headers=headers, data=json.dumps(data))
            print(response)
        except requests.exceptions.RequestException as e:
            print(e)
            print("Server is not available")
    
    def get_updateTime(self)->int:
        return self.config.get_configuration_value(self.__sensorName,"update_time")
      
    
    

