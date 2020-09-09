from gpiozero import Button, LED, Buzzer
from time import sleep
import random

led = LED(20)
buzzer = Buzzer(15)
player_1 = Button(21)
player_2 = Button(4)

time = random.uniform(5, 10)
print(time)
sleep(time)


led.on()

while True:
    if player_1.is_pressed:
        print("Player 1 wins Hell yeah")
        print("Player 2 sucks")
        buzzer.beep()
        break
    if player_2.is_pressed:
        print("Player 2 wins heheheheh ")
        print("Player 1 sucks")
        buzzer.beep()
        break

sleep(2)
buzzer.off()
led.off()