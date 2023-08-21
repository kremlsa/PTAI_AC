import requests
import json
import pprint
import typing
from typing import TypedDict


# r = requests.get("https://blackbox.ssdlc.online/app/api/v1/sites/9fbbf442-4879-48d5-9ecd-ddef9fc34cdc" ,
#                  headers={
#                      "Authorization": "Basic AZMJilHdH7irg9L0o3wyHbwJD7uV0kBGF9OUX16XkzsecTH9oHGrVEtoXQn00A2CVrXDV1vwVdHmohLP"})
# pprint.pprint(json.loads(r.content))

class PtaiUser(TypedDict):
    username: str
    unit: str
    role: str


def load_users():
    with open(filename, 'r') as data_file:
        json_data = data_file.read()

    jsonData = json.loads(json_data)
    print("Datatype of variable: ", type(jsonData))
    print(jsonData[1])



filename = "users.json"
ptai_users = []
load_users()
r = requests.get("https://blackbox.ssdlc.online/app/api/v1/groups" ,
                 headers={
                     "Authorization": "Basic AZMJilHdH7irg9L0o3wyHbwJD7uV0kBGF9OUX16XkzsecTH9oHGrVEtoXQn00A2CVrXDV1vwVdHmohLP"})
pprint.pprint(json.loads(r.content))
