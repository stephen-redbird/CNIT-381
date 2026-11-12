import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://192.168.100.10/restconf/data/ietf-interfaces:interfaces"
headers = {
    "Accept": "application/yang-data+json",
    "content-type": "application/yang-data+json", 
}
basicauth = ("cisco", "cisco123!")

resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
print(resp)                                 #expect <Response [200]>
print(json.dumps(resp.json(), indent=2))    #the interfaces, as JSON