from gpiozero import DistanceSensor,LED
from time import sleep

#DistanceSensor(echo=23, trigger=24,max_distance={FLOAT},threshold_distance={FLOAT})
#max_distance -> This defaults to 1
#threshold_distance -> This is the distance (in meters) ->  trigger the {in_range} and {out_of_range}
sensor = DistanceSensor(23,24,max_distance = 4,threshold_distance=0.3)

led = LED(12)

while True:
    roundedDistance = round(sensor.distance,3)*100
    print "Distance is: ", roundedDistance ,"cm"
    if roundedDistance <= 50:
        led.on()
    else:
        led.off()
    sleep(0.3)