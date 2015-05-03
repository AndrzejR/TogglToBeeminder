"""This module loads and writes to the datapoint id json file."""

import json, logging
from datetime import date

DATAPOINT_FILE = 'datapoint_ids.json'

def load_dp_id(datapoint_date):
    """Loads the datapoint id for the given date.

    Creates the file if it doesn't exist.
    Returns None if no datafile, or no datapoint id for the given date.
    Raises ValueError if the file is broken.
    """
    datapoint_id = None
    try:
        with open(DATAPOINT_FILE, 'r+') as dp_file:
            datapoint_ids = json.load(dp_file)
            for day, dp_id in datapoint_ids.items():
                if day == datapoint_date.isoformat():
                    datapoint_id = dp_id
                    break
            else:
                logging.debug('No datapoint id yet for ' + str(date))

    except FileNotFoundError:
        with open(DATAPOINT_FILE, 'w') as dp_file:
            logging.debug('creating the ' + DATAPOINT_FILE + ' file')
    except ValueError:
        logging.debug('The ' + DATAPOINT_FILE +
                        ' is there, but it looks to be incorrect')
        raise

    return datapoint_id

def write_dp_id(datapoint_id, datapoint_date):
    """Writes the given datapoint id for the given date into the file.

    Creates the file if it doesn't exist.
    """
    with open(DATAPOINT_FILE, 'r+') as dp_file:
        datapoint_ids = {}
        try:
            datapoint_ids = json.load(dp_file)
        except ValueError:
            logging.debug(DATAPOINT_FILE + ' was empty')
        datapoint_ids[datapoint_date.isoformat()] = datapoint_id
        dp_file.seek(0)
        dp_file.truncate()
        json.dump(datapoint_ids, dp_file)


if __name__ == '__main__':

    LOG_DIR = './logs/test/dpfile_'
    LOG_DATE = str(date.today().isoformat().replace('-', ''))
    LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

    logging.basicConfig(filename=LOG_DIR + LOG_DATE + '.log',
                         level=logging.DEBUG, format=LOG_FORMAT)

    TODAY = date.today()
    load_dp_id(TODAY)
    write_dp_id('xXx_test_id_xXx', TODAY)
