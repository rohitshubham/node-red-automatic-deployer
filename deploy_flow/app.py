import requests
import json
import sys
import os

sys.stdout.flush()

total_flows = 0
path_to_jsonfiles = "flows/"
url = 'http://node-red:1880/flows'

def load_file():
    data = []
    for file in os.listdir(path_to_jsonfiles):
        full_filename = "%s/%s" % (path_to_jsonfiles, file)
        with open(full_filename, 'r') as json_file:
            data.append(json.load(json_file))
    return data


print("Loaded file")
data = load_file()
for json_body in data:
    response = requests.post(url, json=json_body)
print("Completed Flows")