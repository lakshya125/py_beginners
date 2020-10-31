import MySQLdb
import time
import datetime
import socket

conn= MySQLdb.connect("LOCAL_HOST","DATABASES","USER","PASSWORD") 
c = conn.cursor() 

c.execute("SELECT * FROM DATABASES")
results = c.fetchall() 
