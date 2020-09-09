#LED Short leg is GROUND 
from gpiozero import Button, LED

#gpiozero = use GPIO Number
button = Button(21)
#25,8,7
led = LED(7)

while True:
    #---------------------------------------
    #button.is_pressed returns TRUE/FALSE
    #if button.is_pressed:
    #    print("Hello")
    #else:
    #    print("Goodbye")

    #---------------------------------------
    #nothing will happen until you press the button and release it
    #button.wait_for_press()
    #print("Pressed")
    #led.on()
    #button.wait_for_release()
    #print("Released")
    #---------------------------------------
    led.blink()
    

    #---------------------------------------


    #---------------------------------------


    #---------------------------------------


    
