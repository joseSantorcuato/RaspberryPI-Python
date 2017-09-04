#Taller e&m
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while(True):

        estado = not GPIO.input(17)
        print "Estado boton: %d" % estado
        sleep(1.0)
	

# Salir con ctrl+c
except KeyboardInterrupt:
    # Limpia configuracion
    GPIO.cleanup()
