#Lab Practical 5
'''Problem Statement:
Write a program using Raspberry-pi to control LED (One or more ON/OFF) or Blinking'''


import time
from gpiozero import LED
led1=LED(7)
led2=LED(22)
led3=LED(23)
led4=LED(25)

while True:
    try:
        led1.off()
        time.sleep(0.5)
        led1.on() 
        led2.off()  
        time.sleep(0.5)
        led2.off()
        led3.on() 
        time.sleep(0.5)
        led3.off()
        led4.on() 
        time.sleep(0.5)
        led4.off() 
    except KeyboardInterrupt:
        print("Closing")
    exit()
    