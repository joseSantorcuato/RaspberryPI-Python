
# -*- coding: utf-8 -*-

import psycopg2
import sys
from time import *
import datetime

   

   
con = None

try:
     
    con = psycopg2.connect("dbname='nuevos_datos' user='usuariopg' host='localhost' password='password'")
    
    cur = con.cursor()
    fecha_actual = datetime.datetime.now()
    ano = fecha_actual.year
    mes = fecha_actual.month
    dia = fecha_actual.day
    fecha_completa = str(ano)+"-"+str(mes)+"-"+str(dia)
  
    cur.execute("INSERT INTO datos (nombre, apellido_p, apellido_m, edad, fecha_ingreso) VALUES (%s, %s, %s , %s, %s)", ('Valeria',  'Labra', 'Osorio', 41, fecha_completa))



    
    con.commit()
    

except psycopg2.DatabaseError, e:
    
    if con:
        con.rollback()
    
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()
