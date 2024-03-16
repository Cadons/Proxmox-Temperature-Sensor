import json
import api.configuration_reader as cr
import requests
from abc import ABC, abstractmethod
class Sensor(ABC):
    
    config: cr.ConfigurationReader=cr.ConfigurationReader()

    def get_value(self) -> json:
        raise NotImplementedError()
    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError()
    @abstractmethod
    def get_id(self) -> str:
        raise NotImplementedError()
    
    def notifyServer(self, inputData)->bool:
        url=self.config.get_configuration_value("monitoring_server_url")
        headers = {'Content-Type': 'application/json'}
        data =inputData
        try:
            response = requests.post(url, headers=headers, data=json.dumps(data))
            print(response)
        except requests.exceptions.RequestException as e:
            print(e)
            print("Server is not available")
    
    def get_updateTime(self)->int:
        return self.config.get_configuration_value("update_time")
    
    

