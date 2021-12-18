# Commonly used functions for data parsing are here
import requests
import xmltodict
import json


class Converter:
    def __init__(self, url):
        self.url = url

    def _get_data(self):
        print("Requesting...")
        response = requests.get(self.url)
        return response.text

    def _convert_xml(self, xml):
        xml_to_dict = xmltodict.parse(xml)
        json_to_dict = json.dumps(xml_to_dict).encode('utf-8')
        parsed_dict_data = json.loads(json_to_dict)
        return parsed_dict_data

    def get_parsed_data(self):
        xml_data = self._get_data()
        dict_data = self._convert_xml(xml_data)
        return dict_data
