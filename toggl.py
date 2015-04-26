import requests
import json
from datetime import date, timedelta

def get_data(date):

	api_token = None
	with open('settings.conf', 'r') as f:
		settings = f.read().splitlines()
		api_token = settings[0]
		user_agent = settings[1]
		workspace_id = settings[2]

	date = date.isoformat()

	# print(yesterday)

	payload = {'user_agent':user_agent, 'workspace_id':workspace_id,
				 'since':date, 'until':date, 'grouping':'clients',
				 'subgrouping':'projects'}

	r = requests.get('https://www.toggl.com/reports/api/v2/summary', auth=(api_token, 'api_token'), params=payload)

	# print(json.dumps(r.json(), sort_keys=True, indent=4, separators=(',',':')))

	# rjson = r.json()

	total_grand_ms = r.json()['total_grand']

	if total_grand_ms is not None:
		total_grand_hours = r.json()['total_grand']/3600000
	else:
		total_grand_hours = 0
		
	print(str(date) + ':' + str(total_grand_hours))

	return total_grand_hours

if __name__ == "__main__":
	today = date.today()
	get_data(today)