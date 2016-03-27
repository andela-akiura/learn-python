"""SQlite3 practice."""
# !/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
from db_util import setup_table, rows


def read_image_from_fs():
    """Read an image from file system."""
    with open("apple.jpg", "rb") as fin:
        return fin.read()


def write_img_to_db():
    """Write an image to test.db."""
    with lite.connect("test.db") as con:
        cur = con.cursor()
        data = read_image_from_fs()
        binary = lite.Binary(data)
        cur.execute("INSERT INTO Images(Data) VALUES (?)", (binary,))


def write_img_to_fs(name):
    """Save an image to the file system."""
    with open(name, "wb") as fout:
        fout.write(data)
