import requests
import json
from datetime import date, timedelta

api_token = None
with open('settings.conf', 'r') as f:
	settings = f.read().splitlines()
	api_token = settings[0]
	user_agent = settings[1]
	workspace_id = settings[2]

yesterday = date.today() - timedelta(days=1)

yesterday = yesterday.isoformat()

# print(yesterday)

payload = {'user_agent':user_agent, 'workspace_id':workspace_id,
			 'since':yesterday, 'until':yesterday, 'grouping':'clients',
			 'subgrouping':'projects'}

r = requests.get('https://www.toggl.com/reports/api/v2/summary', auth=(api_token, 'api_token'), params=payload)

# print(json.dumps(r.json(), sort_keys=True, indent=4, separators=(',',':')))

# rjson = r.json()

total_grand_hours = r.json()['total_grand']/3600000

print(str(yesterday) + ':' + str(total_grand_hours))
