import requests
import json
from datetime import date, timedelta

api_token = None
with open('token.txt', 'r') as f:
	api_token = f.readline()

yesterday = date.today() - timedelta(days=1)

yesterday = yesterday.isoformat()

print(yesterday)

payload = {'user_agent':'andrzej.ruszczewski@gmail.com', 'workspace_id':644218,
			 'since':yesterday, 'until':yesterday, 'grouping':'clients',
			 'subgrouping':'projects'}

r = requests.get('https://www.toggl.com/reports/api/v2/summary', auth=(api_token, 'api_token'), params=payload)

# print(json.dumps(r.json(), sort_keys=True, indent=4, separators=(',',':')))

# rjson = r.json()

total_grand_hours = r.json()['total_grand']/3600000

print(str(yesterday) + ':' + str(total_grand_hours))
