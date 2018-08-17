#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys 
import threading

#script, Select = argv

def rgb(color):
	if color == '1':
		colors = [0x0000FF,0x112233,0x00001F,0x000014,0x000015,0x112233]
		delay = 0.37
	elif color == '2':
		colors = [0x00FF00,0x00FF00,0x000F00]
		delay=0.37
	else:
		colors= [0xFF0000,0x010000]
		delay=0.37
	pins = {'pin_R':11, 'pin_G':12, 'pin_B':13}  # pins is a dict

	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	for i in pins:
		GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
		GPIO.output(pins[i], GPIO.HIGH) # Set pins to high(+3.3V) to off led

	p_R = GPIO.PWM(pins['pin_R'], 4000)  # set Frequece to 2KHz
	p_G = GPIO.PWM(pins['pin_G'], 4000)
	p_B = GPIO.PWM(pins['pin_B'], 4000)

	p_R.start(0)      # Initial duty Cycle = 0(leds off)
	p_G.start(0)
	p_B.start(0)

def map(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def setColor(col):   # For example : col = 0x112233
        R_val = (col & 0x111111) >> 16
        G_val = (col  & 0x001100) >> 8
        B_val = (col & 0x000011) >> 0

        R_val = map(R_val, 0, 255, 0, 50)
        G_val = map(G_val, 0, 255, 0, 100)
        B_val = map(B_val, 0, 255, 0, 100)

        p_R.ChangeDutyCycle(100-R_val)     # Change duty cycle
        p_G.ChangeDutyCycle(100-G_val)
        p_B.ChangeDutyCycle(100-B_val)

try:
        while True:
                for col in colors:
                        setColor(col)
                        time.sleep(delay)
except KeyboardInterrupt:
        p_R.stop()
        p_G.stop()
        p_B.stop()
        for i in pins:
                GPIO.output(pins[i], GPIO.HIGH)    # Turn off all leds
        GPIO.cleanup()
