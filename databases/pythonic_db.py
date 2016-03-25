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

users = ((1, 'Ngeos', 20),
         (2, 'Tei', 21),
         (3, 'John', 23),
         (4, 'Gibbs', 29),
         (5, 'Niki', 33),
         (6, 'Meeek', 28),
         (7, 'Beyonce', 76)
         )
con = lite.connect('test.db')


def setup_table(cursor, table_name, data, **options):
    """Create table table_name and add data to columns."""
    cursor.execute("DROP TABLE IF EXISTS " + table_name)
    cursor.execute("CREATE TABLE " + table_name +
                   " (Id INT, Name TEXT, Amount INT)")
    cursor.executemany("INSERT INTO " + table_name + "VALUES(?, ?, ?)", data)
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("DROP TABLE IF EXISTS Users")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.execute("CREATE TABLE Users(Id INT, Name TEXT, Age INT)")
    cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)
    cur.executemany("INSERT INTO Users VALUES(?, ?, ?)", users)
