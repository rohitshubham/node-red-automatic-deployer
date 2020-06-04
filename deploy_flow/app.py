import requests
import json

def load_file():
    data = {}
    with open('flow/temp.json') as json_file:
        data = json.load(json_file)
    return data

print("Loaded file")
url = 'http://node-red:1880/flows'
response = requests.post(url, json=load_file())
print("Completed Flows")