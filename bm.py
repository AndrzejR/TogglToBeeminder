import requests
import json

with open('bm.conf', 'r') as f:
	settings = f.read().splitlines()
	auth_token = settings[0]
	user = settings[1]
	goal = settings[2]

url = 'https://www.beeminder.com/api/v1/'
url += '/users/' + str(user)
url += '/goals/' + str(goal)
url += '/datapoints.json'

params = {'auth_token':auth_token}


r = requests.get(url, params=params)

# print(json.dumps(r.json(), sort_keys=True, indent=4, separators=(',',':')))

for sth in r.json():
	print(str(sth['daystamp']) + ' : ' + str(sth['value']))