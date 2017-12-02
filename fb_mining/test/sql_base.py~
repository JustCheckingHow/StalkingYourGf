# -*- coding: utf-8 -*-

import sqlite3
import datetime
import time as tm

def today():
	now = datetime.datetime.now()
	date = str(now.day) +"-"+ str(now.month) +"-"+ str(now.year)
	#print(date)
	return date
	
def calc_diff(date):
	now = datetime.datetime.now()
	days = (int(now.day) - int(date[:2]))
	mont = (int(now.month) - int(date[3:5]))*30
	year = (int(now.year) - int(date[6:]))*365
	return days+mont+year	


def set_as_scanned(fbid):
	conn = sqlite3.connect('test_base.db')
	c = conn.cursor()
	
	c.execute("INSERT INTO scan_log VALUES('"+fbid+"', '"+today()+"')")
	
	conn.commit()
	c.close()
	conn.close()
	

def get_oldest_scan():
	conn = sqlite3.connect('test_base.db')
	c = conn.cursor()
	c.execute("SELECT * from scan_log")
	rows = c.fetchall()
	print(rows[0][1])
	

#c.execute("CREATE TABLE osoba(imie text, nazwisko text)")

#c.execute("INSERT INTO person_info VALUES('00120230212', 'Pawel', 'Kulig', 'brak', 'male', '09-10-1996','09-10-1996', '793483169', 'Krakow', 'Krakow', 'brak', 'brak', 'brak')")

#zmienna = "imie"

#c.execute("SELECT "+zmienna+" from person_info WHERE nazwisko = 'Kulig' ")
#rows = c.fetchall()
#print(fetch_from_row(rows[0]))

#for row in rows:

#print(rows[1][0])


#conn.commit()
#c.close()
#conn.close()

#set_as_scanned("pawel.k")
get_oldest_scan()


