
import json
import os
class ConfigurationReader:
    config: json = None
    def __init__(self):
        self.config = self.read_configuration()

    def read_configuration(self):
        dir=os.path.dirname(os.path.abspath(__file__))
        file_path=os.path.join(dir, "config.json")
        jsonFile=open(file_path, "r")
        data = json.load(jsonFile)
        return data

    def get_configuration(self):
        return self.config

    def get_configuration_value(self, key: str):
        return self.config[key]
