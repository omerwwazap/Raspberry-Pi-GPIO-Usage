#LED Short leg is GROUND 
from gpiozero import LED, Button
from time import sleep

led = LED(27)
button = Button(2)

#led.toggle() switches the state of the LED from on to off
while True:
    button.wait_for_press()
    led.toggle()
    sleep(0.5)
led.off()

#or on press -> on
#led = LED(27)
#button = Button(2)
#button.when_pressed = led.on
#button.when_released = led.off
#pause()
    