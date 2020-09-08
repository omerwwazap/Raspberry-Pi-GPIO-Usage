
import RPi.GPIO as GPIO
import time
# blink function
GPIO.setwarnings(False)

def blinkLed(pin_NO):
    GPIO.output(pin_NO, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin_NO, GPIO.LOW)
    time.sleep(1)
    return

# Use Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)
# blink GPIO17 50 times
for i in range(0, 10):
    #blinkLed(11)
    print i + 1,"of",10
GPIO.cleanup()
