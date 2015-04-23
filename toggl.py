import requests
import json

api_token = None
with open('token.txt', 'r') as f:
	api_token = f.readline()

r = requests.get('https://www.toggl.com/api/v8/me', auth=(api_token, 'api_token'))

print(json.dumps(r.json(), sort_keys=True,
				indent=4, separators=(',',':')))