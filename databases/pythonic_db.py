"""SQlite3 practice."""
# !/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

cars = ((1, 'Audi', 52642),
        (2, 'Jeep', 52643),
        (3, 'Benz', 52644),
        (4, 'Koenig', 52645),
        (5, 'Ferrari', 52646),
        (6, 'Bugatti', 52647),
        (7, 'Range Rove', 52642)
        )

con = lite.connect('test.db')

with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)

    data = cur.fetchone()

    print "SQLite version: %s" % data
