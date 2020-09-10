from gpiozero import MotionSensor, Buzzer
from signal import pause
from time import sleep

pir = MotionSensor(4)
buzzer = Buzzer(16)

#This probably a terrible implementation but hey it works and its my idea :)
while True:
    pir.wait_for_motion()
    print("Alarm ON!")
    buzzer.beep()
    pir.wait_for_no_motion()
    print("Alarm Off!")
    buzzer.off()