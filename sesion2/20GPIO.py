
#Taller e&m
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT)

print "Prendido"

GPIO.output(18,GPIO.HIGH)

time.sleep(1)

print "Apagado"

GPIO.output(18,GPIO.LOW)
