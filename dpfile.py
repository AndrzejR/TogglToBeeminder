import json, logging
from datetime import date

DATAPOINT_FILE = 'datapoint_ids.json'

def load_dp_id(date):
	datapoint_id = None
	try:
		with open(DATAPOINT_FILE, 'r+') as f:			
			datapoint_ids = json.load(f)
			for day, dp_id in datapoint_ids.items():
				if day == date.isoformat():
					datapoint_id = dp_id
					break
			else:
				logging.debug('No datapoint id yet for ' + str(date))

	except FileNotFoundError:
		with open(DATAPOINT_FILE, 'w') as f:
			logging.debug('creating the ' + DATAPOINT_FILE + ' file')
	except ValueError:
		logging.debug('The ' + DATAPOINT_FILE + ' is there, but it looks to be incorrect')
		raise

	return datapoint_id

def write_dp_id(datapoint_id, date):
	with open(DATAPOINT_FILE, 'r+') as f:
		datapoint_ids = {}
		try:
			datapoint_ids = json.load(f)
		except ValueError:
			logging.debug(DATAPOINT_FILE + ' was empty')
		datapoint_ids[date.isoformat()] = datapoint_id
		f.seek(0)
		f.truncate()
		json.dump(datapoint_ids, f)


if __name__ == '__main__':

	logging.basicConfig(filename='./logs/test/dpfile_' + str(date.today().isoformat().replace('-','')) + '.log', level=logging.DEBUG,
						format='%(asctime)s - %(levelname)s -  %(message)s')

	today = date.today()
	load_dp_id(today)
	write_dp_id('xXx_test_id_xXx', today)
