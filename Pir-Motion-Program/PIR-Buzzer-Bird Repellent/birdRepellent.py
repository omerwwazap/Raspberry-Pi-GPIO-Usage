from gpiozero import MotionSensor, Buzzer
from signal import pause
from time import sleep

pir = MotionSensor(4)
buzzer = Buzzer(16)

pir.when_motion =  buzzer.on()
pir.when_no_motion = buzzer.off()

pause()