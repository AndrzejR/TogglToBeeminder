"""This is the main executable meant to be scheduled."""

import logging
import bm, toggl, db
from datetime import date

DEBUG = False # set to True not to insert or update anything in Beeminder

LOG_DIR = './logs/'
LOG_DATE = str(date.today().isoformat().replace('-', ''))
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

logging.basicConfig(filename=LOG_DIR + LOG_DATE + '.log',
                    level=logging.DEBUG, format=LOG_FORMAT)

logging.info("****************** Starting a new run ******************")

TODAY = date.today()

TOGGL_DATA = toggl.get_data(TODAY)
logging.debug("Today's data from toggl: " + str(TOGGL_DATA))


if TOGGL_DATA != 0:

    BM = bm.BeemAPI()

    # do we have a datapoint id for today in the file?
    DATAPOINT_ID = db.load_dp_id(TODAY)

    # not in the file? maybe there already is a datapoint in BM?
    if DATAPOINT_ID is None:
        logging.debug("No DP in the file, let's check in BM.")
        BM_DATA = BM.get_data(TODAY)
        if BM_DATA is not None:
            logging.debug('BM returned id: ' + str(BM_DATA.id))
            DATAPOINT_ID = BM_DATA.id
        else:
            logging.debug('No data returned from BM.')

        # it was in BM but not in the file, let's put it there
        if DATAPOINT_ID is not None:
            db.write_dp_id(DATAPOINT_ID, TODAY)

    # if no data for the day in BM, insert needed
    if DATAPOINT_ID is None:
        logging.debug('datapoint_id is None. Will insert into bm.')
        NEW_DATAPOINT_ID = BM.insert(data=TOGGL_DATA, debug=DEBUG)
        db.write_dp_id(NEW_DATAPOINT_ID, TODAY)
    # we have a datapoint, update
    else:
        logging.debug('Updating datapoint ' + str(DATAPOINT_ID))
        BM.update(datapoint_id=DATAPOINT_ID, data=TOGGL_DATA, debug=DEBUG)


else:
    logging.warning("No data for toggl for today.")




# tomorrow = today + timedelta(days=1)

# print("Tomorrow's data from bm: " + str(bm.get_data(tomorrow)))

# print("Tomorrow's data from toggl: " + str(toggl.get_data(tomorrow)))

# what can go wrong? I don't want to add points if there's one already
# what about running not for today's date? if one of the endpoints goes down?
# begin with a check for which days there are already bm datapoints?
# back to a week or two?
# or just create a local DCM storing this data?
