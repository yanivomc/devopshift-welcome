import httpx
import json
from pprint import pprint

response = httpx.get('https://jsonplaceholder.typicode.com/users')
pprint(response)
users = response.json()
for user in users:
    pprint(user['name'])
    