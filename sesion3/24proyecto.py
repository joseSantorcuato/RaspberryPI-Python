#Taller e&m
# -*- coding: utf-8 -*-

#Listas

import RPi.GPIO as GPIO
import time
import re

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)




for i in range (0,2):
   print(i)
   print "Prendido"
   GPIO.output(5,GPIO.HIGH)
   GPIO.output(6,GPIO.HIGH)
   GPIO.output(13,GPIO.HIGH)
   GPIO.output(19,GPIO.HIGH)
   GPIO.output(26,GPIO.HIGH)
   time.sleep(1)
   print " "
   print "Apagado"

   GPIO.output(5,GPIO.LOW)
   GPIO.output(6,GPIO.LOW)
   GPIO.output(13,GPIO.LOW)
   GPIO.output(19,GPIO.LOW)
   GPIO.output(26,GPIO.LOW)

   time.sleep(1)

lista_leds = [5, 6, 13, 19, 26]

print lista_leds[0:5]



a= input("Ingrese un el valor desde donde desea comenzar la busqueda: ")
print a

b= input("Ingrese un el valor posterior a la posicion en que desea realizar la busqueda: ")
print b

ast = str(a)
bst = str(b)

aa = int(a)
bb = int(b)

print "["+ast+":"+bst+"] : ""\t", lista_leds[a:b]

GPIO.output(lista_leds[aa:bb], GPIO.HIGH)
time.sleep(3)

GPIO.output(lista_leds[aa:bb], GPIO.LOW)

   























