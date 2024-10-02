import requests
import json
import jsonpath

url ="https://reqres.in/api/users?page=2"

response = requests.get(url);
'''
print(response)
print(response.content)
print("---------------------------------")
print(response.headers)

'''

#Jsonpath
jsonres = json.loads(response.text)
print(jsonres)

pages = jsonpath.jsonpath(jsonres,"total")
print(pages[0])
assert pages[0] ==12
