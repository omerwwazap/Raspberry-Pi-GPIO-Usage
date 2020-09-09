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


#With Borad Numbers 1 2
#                   3 4
#GPIO.setmode(GPIO.BOARD)

#With GPIO Codes   GPIO02
#                  GPIO03
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BCM)

# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)
# blink GPIO17 50 times
for i in range(0, 10):
    blinkLed(11)
    print i+1,"of",10
GPIO.cleanup()

#Alternatively
#from gpiozero import LED
#from time import sleep

#gpiozero uses GPIO codes
#led = LED(11) #GPIO11

#for i in range(0, 10):
#    led.on()
#    print i+1,"of",10
#    sleep(1)
#    led.off()
#    sleep(1)
