
# -*- coding: utf-8 -*-

import psycopg2
import sys
from time import *
import datetime




conn = None

try:
    connect_str = "dbname='mis_datos' user='pguser' host='localhost' " + \
                  "password='pass'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    fecha_actual = datetime.datetime.now()
    ano = fecha_actual.year
    mes = fecha_actual.month
    dia = fecha_actual.day
    fecha_completa = str(ano)+"-"+str(mes)+"-"+str(dia)

    cursor.execute("INSERT INTO datos (nombre, apellido_p, apellido_m, edad, fecha_ingreso) VALUES (%s, %s, %s , %s, %s)", ('Carmen',  'Moreno', 'Soto', 43, fecha_completa))




    conn.commit()


except Exception as e:
    print("Error, revisa conexion, usuario o base de datos")
    print(e)
