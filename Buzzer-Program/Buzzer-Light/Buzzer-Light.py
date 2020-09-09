# LED Short leg is GROUND
from gpiozero import Button, LED, Buzzer, TrafficLights, Buzzer
from time import sleep

# gpiozero = use GPIO Number
button = Button(21)
# 25,8,7
#led = LED(7)
lights = TrafficLights(25, 8, 7)
buzzer = Buzzer(15)

while True:
    # ---------------------------------------
    # button.is_pressed returns TRUE/FALSE
    # if button.is_pressed:
    #    print("Hello")
    # else:
    #    print("Goodbye")

    # ---------------------------------------
    # nothing will happen until you press the button and release it
    # button.wait_for_press()
    # print("Pressed")
    # led.on()
    # button.wait_for_release()
    # print("Released")
    # ---------------------------------------
    # LED blink on and off until the button is pressed
    # Than it will turn off completely.
    # When the button is released, it will start blinking again.
    # led.blink()
    # button.wait_for_press()
    # led.off()
    # button.wait_for_release()
    # ---------------------------------------
    # led.blink(2, 2) - 2 seconds on, 2 seconds off
    # led.blink(0.5, 0.5) - half a second on, half a second off
    # led.blink(0.1, 0.2) - one tenth of a second on, one fifth of a second
    # ---------------------------------------
    # on/off all light in lights = TrafficLights(25,8,7)
    # button.wait_for_press()
    # lights.on()
    # button.wait_for_release()
    # lights.off()
    # ---------------------------------------
    # Lİghts on -> press button lights off and Buzzer on -> vice versa
    # lights.on()
    # buzzer.off()
    # button.wait_for_press()
    # lights.off()
    # buzzer.on()
    # button.wait_for_release()
    # ---------------------------------------
    # since TrafficLights(red, amber, and green) we can do lights.red.on() etc.
    # lights.green.on()
    # sleep(1)
    # lights.amber.on()
    # sleep(1)
    # lights.red.on()
    # sleep(1)
    # lights.off()
    # ---------------------------------------
    # Full TrafficLights with sound
    button.wait_for_press()
    lights.green.on()
    sleep(3)

    lights.amber.on()
    buzzer.beep()
    sleep(3)

    lights.green.off()
    lights.amber.off()
    lights.red.on()
    buzzer.off()
    sleep(3)

    lights.amber.on()
    lights.red.on()
    sleep(1)

    lights.green.on()
    lights.amber.off()
    lights.red.off()
    sleep(1)
    lights.off()
    # ---------------------------------------
