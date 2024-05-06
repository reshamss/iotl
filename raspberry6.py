/*Lab Practical 6
Problem Statement:
Create a program that illuminates the green LED if the counter is less than 100, illuminate the yellow LED if 
the counter is between 101 and 200 and illuminates the red LED if the counter is greater than 200.*/
//Code:
import time
from gpiozero import LED
led1 = LED(7)
led2 = LED(22)
led3 = LED(23)
number=0
while True:
 time.sleep(0.2)
 if number<=100:
 led1.off()
 led2.on()
 led3.on()
 elif number>201 and number<=300:
 led1.on()
 led2.off()
 led3.on()
 elif number>101 and number<=200:
 led1.on()
 led2.on()
 led3.off()
 
 number=number+1
