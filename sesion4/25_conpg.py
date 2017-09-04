#Taller e&m
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None

try:

    con = psycopg2.connect("dbname='nuevos_datos' user='usuariopg' host='localhost' password='password'")
    cur = con.cursor()
    cur.execute('SELECT version()')
    ver = cur.fetchone()
    print ver


except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)


finally:

    if con:
        con.close()
