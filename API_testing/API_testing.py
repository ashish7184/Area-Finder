import requests,json

payload= {}
payload["Latitude"] ="19.1108952"
payload["Longitude"] ="73.016111"
json_payload = json.dumps(payload)
json_payload = json.loads(json_payload)
response = requests.post('http://192.168.38.47:5001/Area_Finder',verify=False,json=json_payload)

print("Status code: ", response.status_code)
print(response.text)
