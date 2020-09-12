from gpiozero import DistanceSensor
from time import sleep
#DistanceSensor(echo=23, trigger=24,max_distance={FLOAT},i)
sensor = DistanceSensor(23,24,max_distance=4)

while True:
    roundedDistance = round(sensor.distance,3)
    print "Distance is: ", roundedDistance*100 ,"cm"
    print "Distance is: ", round(sensor.distance,3) ,"m"
    sleep(1)