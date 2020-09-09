#button to another GND pin and GPIO pin 2
#LED Short leg is GROUND 
from gpiozero import Button
#button is on pin 2.
button = Button(2)
# button is pushed
button.wait_for_press()
print('You pushed me')