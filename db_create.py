"""This is a one-off script to create the sqlite3 db."""

import sqlite3

DATABASE_FILE = 'ttbm.db'
CONNECTION = sqlite3.connect(DATABASE_FILE)

CURSOR = CONNECTION.cursor()

CURSOR.execute('''create table if not exists bm_datapoint
               (id text primary key
               , value real
               , timestamp integer
               , updated_at integer
               , daystamp text
               , comment text
               , requestid text)
               ''')

CURSOR.execute('''create table if not exists parameter
               (param_name text primary key
               , param_value text)
               ''')

CONNECTION.commit()