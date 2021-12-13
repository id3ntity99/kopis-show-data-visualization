# Commonly used functions for data parsing are here
import requests
import xmltodict
import json


# Convert XML to JSON to Dict and return Dict
def convert_xml(xml):
    xml_to_dict = xmltodict.parse(xml)
    json_to_dict = json.dumps(xml_to_dict).encode('utf-8')
    parsed_dict_data = json.loads(json_to_dict)
    return parsed_dict_data


# Call KOPIS API and get XML texts.
def get_data(URL):
    print("Requesting Please Wait ...")
    response = requests.get(URL)
    return response.text


def get_parsed_data(URL):
    xml_data = get_data(URL)
    dict_data = convert_xml(xml_data)
    return dict_data
