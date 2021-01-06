import RPi.GPIO as GPIO
import time #adds time library

GPIO.setwarnings(False) # Fixes errors, got this from graham
leds = [38] # Adds the pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(leds, GPIO.OUT) # sets the pins to output so it can eventually blink

for i in range(0, 10): # blinks 10 times.
	GPIO.output(leds, 1)
	time.sleep(0.5) 
	GPIO.output(leds, 0)
	time.sleep(0.5)
	print("Harry is cool")
