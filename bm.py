import requests
import json
from datetime import date, timedelta
from collections import namedtuple
import logging

BMDatapoint = namedtuple("BMDatapoint", "id, value")

class BeemAPI:

	URL = 'https://www.beeminder.com/api/v1/'

	def __init__(self):
		with open('bm.conf', 'r') as f:
			settings = f.read().splitlines()
			self.auth_token = settings[0]
			self.user = settings[1]
			self.goal = settings[2]

	def is_updated(self):

		last_updated = 0

		try:
			with open('updated_at', 'r') as f:
				last_updated = int(f.readline())
		except Exception:
			with open('updated_at', 'w') as f:
				f.write(str(last_updated))

		url = BeemAPI.URL
		url += '/users/' + str(self.user) + '.json'
		params = {'auth_token':self.auth_token}		

		r = requests.get(url, params=params)

		logging.debug(json.dumps(r.json(), sort_keys=True, indent=4, separators=(',',':')))

		j = r.json()

		updated_at = int(j['updated_at'])

		logging.debug('updated_at is: ' + str(updated_at))

		if last_updated >= updated_at:
			logging.debug('last_updated >= updated_at')
			return False
		else:
			logging.debug('last_updated < updated_at')
			with open('updated_at', 'w') as f:
				f.write(str(updated_at))
			return True
		


	def get_data(self, date):	
		date = date.isoformat().replace('-', '')
		logging.debug(date)

		
		url = BeemAPIURL
		url += '/users/' + str(self.user)
		url += '/goals/' + str(self.goal)
		url += '/datapoints.json'

		params = {'auth_token':self.auth_token}


		r = requests.get(url, params=params)

		logging.debug(json.dumps(r.json(), sort_keys=True, indent=4, separators=(',',':')))

		result = None
		for sth in r.json():
			if sth['daystamp'] == date:
				logging.debug('datapoints id is: ' + str(sth['id']))				
				logging.debug('datapoint is: '+str(sth['daystamp']) + ' : ' + str(sth['value']))							
				result = BMDatapoint(sth['id'], sth['value'])

		return result

	def insert(data):
		pass

	def update(id, data):
		pass

if __name__ == '__main__':
	
	logging.basicConfig(filename='./logs/test/bm_' + str(date.today().isoformat().replace('-','')) + '.log', level=logging.DEBUG,
						format='%(asctime)s - %(levelname)s -  %(message)s')
	day = date.today() - timedelta(days=1)
	bm = BeemAPI()
	# bm_data = bm.get_data(day)
	# logging.debug("data from bm: " + str(bm_data))
	# logging.debug("data from bm: " + str(bm_data.id))
	# logging.debug("data from bm: " + str(bm_data.value))
	bm.is_updated()