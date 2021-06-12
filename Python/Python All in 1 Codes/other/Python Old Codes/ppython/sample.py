#from typing import Dict, Text, Any, List, Union, Optional
import requests
from requests.auth import HTTPBasicAuth
import json
import re


url = 'https://sandbox.webcomcpq.com/wsAPI/wssrv.asmx'
username = 'X0105453'
password = 'Knack@123'
auth_values = (username, password)
# Empid = tracker.get_slot("empID")
value = {
    "user": "6723",
    "approvalStatus":"approved"
}
response = requests.post(url, data=json.dumps(value), auth=HTTPBasicAuth(username, password))
str1 = ""
timeSheetVar = ""
json_data = response.json()
print(json_data)
if response.status_code != 200:
            # This means something went wrong.
            # raise ApiError('GET /tasks/ {}'.format(response.status_code))
    #print(response.status_code)
    pass
else:
    json_data = response.json()
    timesheetcount = len(json_data)
    print(json_data)