import requests
import json


r = requests.get('https://www.toggl.com/api/v8/me', auth=('59516aa742fa8eb8d29dd596d489448b', 'api_token'))

print(json.dumps(r.json(), sort_keys=True,
				indent=4, separators=(',',':')))