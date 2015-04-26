# this is the main job meant to be scheduled
import bm, toggl
from datetime import date, timedelta
import logging

today = date.today()

logging.basicConfig(filename='./logs/' + str(today.isoformat().replace('-', '')) + '.log',
					 level=logging.DEBUG, format='%(asctime)s - %(levelname)s -  %(message)s')

logging.debug("Today's data from bm: " + str(bm.get_data(today)))

logging.debug("Today's data from toggl: " + str(toggl.get_data(today)))

if toggl.get_data(today) != 0:
	if bm.get_data(today) is not None:
		logging.debug('Will update bm.')
	else:
		logging.debug('Will insert into bm.')
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