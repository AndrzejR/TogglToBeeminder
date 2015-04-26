# this is the main job meant to be scheduled
import bm, toggl
from datetime import date, timedelta

# check date

today = date.today()

print(bm.get_data(today))

print(toggl.get_data(today))

tomorrow = today + timedelta(days=1)

print(bm.get_data(tomorrow))

print(toggl.get_data(tomorrow))


# get datapoint from toggl

# check if datapoint for this day exists in bm

# upsert data from toggl


# what can go wrong? I don't want to add points if there's one already
# what about running not for today's date? if one of the endpoints goes down?
# begin with a check for which days there are already bm datapoints? back to a week or two?
# or just create a local DCM storing this data?