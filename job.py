"""This is the main executable meant to be scheduled."""

import logging
import json
import bm, toggl, dpfile
from datetime import date, timedelta
from collections import namedtuple

debug = True # set to True not to insert or update anything in Beeminder

logging.basicConfig(filename='./logs/' + str(date.today().isoformat().replace('-', '')) + '.log',
					 level=logging.DEBUG, format='%(asctime)s - %(levelname)s -  %(message)s')
logging.info("****************** Starting a new run ******************")

today = date.today()

toggl_data = toggl.get_data(today)
logging.debug("Today's data from toggl: " + str(toggl_data))


if toggl_data != 0:

	bm = bm.BeemAPI()

	# do we have a datapoint id for today in the file?
	datapoint_id = dpfile.load_dp_id(today)

	# not in the file? maybe there already is a datapoint in BM?
	if datapoint_id is None:
		logging.debug("No DP in the file, let's check in BM.")		
		bm_data = bm.get_data(today)
		logging.debug('BM returned id: ' + str(bm_data.id))
		datapoint_id = bm_data.id

		# it was in BM but not in the file, let's put it there
		if datapoint_id is not None:
			dpfile.write_dp_id(datapoint_id, today)

	# if no data for the day in BM, insert needed
	if datapoint_id is None:
		logging.debug('datapoint_id is None. Will insert into bm.')
		new_datapoint_id = bm.insert(data=toggl_data, debug=debug)
		dpfile.write_dp_id(new_datapoint_id, today)
	# we have a datapoint, update
	else:
		logging.debug('Updating datapoint ' + str(datapoint_id))
		bm.update(datapoint_id=datapoint_id, data=toggl_data, debug=debug)
	
		
else:
	logging.warning("No data for toggl for today.")




# tomorrow = today + timedelta(days=1)

# print("Tomorrow's data from bm: " + str(bm.get_data(tomorrow)))

# print("Tomorrow's data from toggl: " + str(toggl.get_data(tomorrow)))



# check date

# get datapoint from toggl

# check if datapoint for this day exists in bm

# upsert data from toggl


# what can go wrong? I don't want to add points if there's one already
# what about running not for today's date? if one of the endpoints goes down?
# begin with a check for which days there are already bm datapoints? back to a week or two?
# or just create a local DCM storing this data?