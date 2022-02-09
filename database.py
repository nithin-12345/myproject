import sqlite3

conn = sqlite3.connect('bhhsamb.db')
curr = conn.cursor()

curr.execute(""" create table bhhsamb_tb(
    name text,
    image_url url,
    contact_details text)""")

conn.commit()
conn.close()
