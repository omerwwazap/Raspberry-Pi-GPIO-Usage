#LED Short leg is GROUND 
import RPi.GPIO as GPIO
import time


#With Borad Numbers 1 2
#                   3 4
#GPIO.setmode(GPIO.BOARD)

#With GPIO Codes   GPIO02
#                  GPIO03
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BCM)

#Disable Usage warnigs etc.
GPIO.setwarnings(False)

#Low 0volts High 3.3volts
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

#pull_up_down = Change?
#initilize sietch change?
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Blink 5 times
for i in range(5):
    GPIO.output(18, GPIO.HIGH)
    time.sleep(.1)
    GPIO.output(18, GPIO.LOW)
    time.sleep(.1)

#Switch function
led_on = False
def switch(ev=None):
    global led_on
    #switch true to false, false to true
    led_on = not led_on
    GPIO.output(18, GPIO.HIGH if led_on else GPIO.LOW)

#catch siwtch press
#FALLING open on push
#RISING open on lift
#bbouncetime stop getting event for 300ms
GPIO.add_event_detect(23, GPIO.RISING, callback=switch, bouncetime=300)

#if not infine loop will leav program.
#while True:
#    time.sleep(1)
for secs in range(20, 0, -1):
    time.sleep(1)
    if secs % 10 == 0:
        print "Time remaining:", secs, "seconds until shutdown"
    if secs == 1:
        print "Bye Bye"
        exit()