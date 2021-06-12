from requests.auth import HTTPBasicAuth
import requests
url = 'https://b2bqa.amat.com/receiveQuoteFromCPQDEV'
final_data1 = '<root><customer>roy</customer></root>'

username = "intg-cpquser"
password = "cpquser"
response = requests.post(url,final_data1, auth=HTTPBasicAuth(username, password))
print(response)