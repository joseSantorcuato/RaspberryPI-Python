#Taller e&m
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

led_gpio = 4
GPIO.setup(led_gpio, GPIO.OUT)

for _ in range(10):

	GPIO.output(led_gpio, not GPIO.input(led_gpio))
	sleep(0.1)
GPIO.cleanup()
