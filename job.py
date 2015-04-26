# this is the main job meant to be scheduled
import bm, toggl
from datetime import date, timedelta
import logging
from collections import namedtuple

debug = False # set to True not to insert or update anything in Beeminder

logging.basicConfig(filename='./logs/' + str(date.today().isoformat().replace('-', '')) + '.log',
					 level=logging.DEBUG, format='%(asctime)s - %(levelname)s -  %(message)s')
logging.info("****************** Starting a new run ******************")

today = date.today()

# check BM for updated_at - needs some kind of dcm to make sense

bm = bm.BeemAPI()

bm_data = bm.get_data(today)


toggl_data = toggl.get_data(today)
logging.debug("Today's data from toggl: " + str(toggl_data))

if toggl_data != 0:
	if bm_data is not None:
		logging.debug("Today's data from bm: " + str(bm_data))
		logging.debug("Today's data from bm: " + str(bm_data.id))
		logging.debug("Today's data from bm: " + str(bm_data.value))
		logging.debug('Will update bm.')
		bm.update(datapoint_id=bm_data.id, data=toggl_data, debug=debug)
	else:
		logging.debug('bm_data is None. Will insert into bm.')
		bm.insert(data=toggl_data, debug=debug)
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