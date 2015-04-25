import requests
import json

api_token = None
with open('token.txt', 'r') as f:
	api_token = f.readline()

payload = {'user_agent':'andrzej.ruszczewski@gmail.com', 'workspace_id':644218,
			 'since':'2015-04-24', 'until':'2015-04-24', 'grouping':'clients',
			 'subgrouping':'projects'}

r = requests.get('https://www.toggl.com/reports/api/v2/summary', auth=(api_token, 'api_token'), params=payload)

print(json.dumps(r.json(), sort_keys=True,
				indent=4, separators=(',',':')))

rjson = r.json()

for key,val in rjson.items():
	print(str(key) + ':' + str(val))

total_grand_hours = rjson['total_grand']/3600000

