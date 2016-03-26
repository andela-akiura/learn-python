"""SQlite3 practice."""
# !/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
from db_util import setup_table

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

with con:
    cur = con.cursor()
    setup_table(cur, "Users", users, ID="INT", Name="Text", Age="INT")
    setup_table(cur, "Cars", cars, ID="INT", Name="Text", Price="INT")
