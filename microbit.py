from microbit import *

#controlling microservo with PIR sensor input

pin0.set_analog_period(20)
#set time period to 20ms
while True:
#Read PIR for input, values are 1 or 0
#If value detected turn servo 180 degrees 
   if pin1.read_digital():
      pin0.write_analog(180)
      sleep(1000)
#Else do not move servo      
   else:
      pin0.write_analog(1)
      sleep(1000)
      