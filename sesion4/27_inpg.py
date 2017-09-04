#Taller e&m
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None

try:

    con = psycopg2.connect("dbname='nuevos_datos' user='usuariopg' host='localhost' password='password'")
    cur = con.cursor()
    cur.execute("INSERT INTO datos VALUES('Antonio','Mondaca','Tapia',21,'2017-03-19 15:38:54.561004')")
    con.commit()


except psycopg2.DatabaseError, e:

    if con:
        con.rollback()

    print 'Error %s' % e
    sys.exit(1)


finally:

    if con:
        con.close()
