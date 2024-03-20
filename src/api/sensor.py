import json
import random
import api.configuration_reader as cr
import requests
from abc import ABC, abstractmethod
import influxdb_client, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
class Sensor(ABC):
    id = None
    name = None
    __sensorName=None
    __org = None
    __influx_url = None
    __api_url = None
    __token = None
    __write_client=None
    onApi=False
    onInflux=False
    
    config: cr.ConfigurationReader=cr.ConfigurationReader()
    def __init__(self, id: str, name: str, sensorName:str):
        self.id = id
        self.name = name
        self.__sensorName=sensorName
        if self.config.get_configuration_value(self.__sensorName,"load_on_api") == True:
            self.onApi=True
            self.__api_url = "http://localhost:5000/api/sensor"
        

        if self.config.get_configuration_value(self.__sensorName,"load_on_influx") == True:
            self.onInflux=True
            self.__org = self.config.get_configuration_value(self.__sensorName,"influx_org")
            self.__influx_url = self.config.get_configuration_value(self.__sensorName,"influx_server_url")
            self.__token = self.config.get_configuration_value(self.__sensorName,"influx_token")
            self.__write_client=influxdb_client.InfluxDBClient(url=self.__influx_url, token=self.__token, org=self.__org)
        
        
    @abstractmethod
    def get_value(self) -> json:
        raise NotImplementedError()

    def get_name(self) -> str:
        return self.name
 
    def get_id(self) -> str:
        return self.id
    
    def notifyServer(self, inputData,url=None)->bool:
        if url == None:
            url=self.__api_url
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
      
    def loadInfluxDB(self,name="", value=-1):
      
        bucket = self.config.get_configuration_value(self.__sensorName,"influx_bucket")
        self.__write_api = self.__write_client.write_api(write_options=SYNCHRONOUS)
        if value == -1:
            value=10
        
        point=Point(name).tag("sensor",self.get_name()).field("value",value).time(time.time_ns(), WritePrecision.NS)
        self.__write_api.write(bucket=bucket, record=point)
        
    

