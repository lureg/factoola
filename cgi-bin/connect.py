#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import MySQLdb
import json,time,sys,datetime
from warnings import filterwarnings

filterwarnings('ignore', category = MySQLdb.Warning)

config = {
	'database': 'factoola',
	'user': 'root',
	'password': 'ubuntu',
	'host': 'localhost',
	'port': 3306,
}

def escape_sql_injection(elem):
	if isinstance(elem, str):
		elem = str(MySQLdb.escape_string(elem))
	elif isinstance(elem, dict):
		aux = {}
		for key in elem:
			key = str(MySQLdb.escape_string(key))
			aux[key] = str(MySQLdb.escape_string(elem[key]))
		elem = aux
	else:
		print "escape_sql_injection ERROR: INVALID TYPE"
	return elem

def time_stamp():
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
	return st 

def sql_action(query):
	response = []
	cnx = MySQLdb.connect(host = config['host'], db = config['database'], user = config['user'], passwd = config['password'], port  = config['port'])
	cursor = cnx.cursor(MySQLdb.cursors.DictCursor)
	if query:
		cursor.execute(query)
		response = cursor.fetchall()
		cursor.close()
		cnx.close()
	return response