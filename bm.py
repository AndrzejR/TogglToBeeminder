import requests
import json
from datetime import date, timedelta


def get_data(date):	
	date = date.isoformat().replace('-', '')
	# print(date)

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

	result = None
	for sth in r.json():
		if sth['daystamp'] == date:
			print(str(sth['daystamp']) + ' : ' + str(sth['value']))
			result = sth['value']

	return result

if __name__ == '__main__':
	today = date.today()
	get_data(today)