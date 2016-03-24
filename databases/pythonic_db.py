"""SQlite3 practice."""
# !/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('test.db')

with con:
    cur = con.cursor()
    cur.execute("SELECT SQLITE_VERSION()")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.execute("INSERT INTO Cars VALUES(1, 'Audi', 52642)")
    cur.execute("INSERT INTO Cars VALUES(2, 'Jeep', 52643)")
    cur.execute("INSERT INTO Cars VALUES(3, 'Benz', 52644)")
    cur.execute("INSERT INTO Cars VALUES(4, 'Koenig', 52645)")
    cur.execute("INSERT INTO Cars VALUES(5, 'Ferrari', 52646)")
    cur.execute("INSERT INTO Cars VALUES(6, 'Bugatti', 52647)")
    cur.execute("INSERT INTO Cars VALUES(7, 'Range Rover', 52642)")

    data = cur.fetchone()

    print "SQLite version: %s" % data
