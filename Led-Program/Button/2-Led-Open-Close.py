from gpiozero import LED
from time import sleep

led = LED(27)

for i in range(0, 10):
    led.on()
    print i+1,"of",10
    sleep(1)
    led.off()
    sleep(1)

#cool
#while True:
#    LED.blink()