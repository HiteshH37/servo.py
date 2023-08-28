#Author:Hitesh H 
from machine import Pin, PWM
#A simple class for controlling a 9g servo with the Raspberry Pi Pico
class Servo:
    def __init__(self,value):
        self.s = PWM(Pin(value))
        self.s.freq(50)
    
    def angle(self, x):
        #For custom angle of rotation 
        y = ((320 / 9) * x) + 1800
        y = round(y, 4)
        self.s.duty_u16(int(y))

    def midpos(self):
        #Makes the servo to rotate the blade to mid position
        """Note for calibration:for setting up the mid position remove the blade then call midpos(), 
           the servo will rotate to the mid position,replace the blade in mid position"""
        self.s.duty_u16(5000)
    
    def inpos(self):
        #Makes the servo to rotate the blade to initial position (0 degree)
        self.s.duty_u16(1800)
    
    def extpos(self):
        #Makes the servo to rotate the blade to extreme position (180 degree)
        self.s.duty_u16(8200)
