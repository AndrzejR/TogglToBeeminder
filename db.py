"""This module is intended to save datapoints (or more) to a db."""

import sqlite3
import logging
from datetime import date

DATABASE_FILE = 'ttbm.db'

def load_dp_id(datapoint_date):
    """Loads the datapoint id for the given date.

    ??? Creates the file if it doesn't exist.
    Returns None if no datafile, or no datapoint id for the given date.
    ??? Raises ValueError if the file is broken.
    """
    datapoint_id = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cur = conn.cursor()

        # cur.execute('''create table datapoint
        #                 (date text, id text)''')
        dp_t = datapoint_date,
        cur.execute('select id from datapoint where date=?',
                     dp_t)
        datapoint_id = cur.fetchone()
        print(datapoint_id)

    except Exception as exc:
        print(exc)

    return datapoint_id

def write_dp_id(datapoint_id, datapoint_date):
    """Writes the given datapoint id for the given date into the db."""
    raise NotImplementedError('Not implemented yet.')


if __name__ == '__main__':

    LOG_DIR = './logs/test/db_'
    LOG_DATE = str(date.today().isoformat().replace('-', ''))
    LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

    logging.basicConfig(filename=LOG_DIR + LOG_DATE + '.log',
                         level=logging.DEBUG, format=LOG_FORMAT)

    TODAY = date.today()
    load_dp_id(TODAY)
    # write_dp_id('xXx_test_id_xXx', TODAY)
    load_dp_id(TODAY)