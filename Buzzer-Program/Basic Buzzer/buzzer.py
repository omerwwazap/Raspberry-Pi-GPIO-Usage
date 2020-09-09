from gpiozero import Buzzer
from time import sleep

#In GPIO Zero, a Buzzer works exactly like an LED
buzzer = Buzzer(17)
while True:
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(1)
buzzer.off()
#cool
# while True:
#    buzzer.beep()   