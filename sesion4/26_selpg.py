#Taller e&m
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None

try:

    con = psycopg2.connect("dbname='nuevos_datos' user='pguser' host='localhost' password='pass'")
    cur = con.cursor()
    cur.execute('SELECT * from datos')
    ver = cur.fetchall()
    print ver


except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)


finally:

    if con:
        con.close()
