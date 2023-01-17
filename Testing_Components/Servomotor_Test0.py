from time import sleep
from machine import Pin, PWM

pwm0 = PWM(Pin(0))
pwm2 = PWM(Pin(1))
pwm1 = PWM(Pin(2))
pwm3 = PWM(Pin(3))

pwm0.freq(50)
pwm1.freq(50)
pwm2.freq(50)
pwm3.freq(50)
def positionServos():
    #positions = [[6000, 6300, 9000, 3700], [6000, 7000, 9000, 3500], [8000, 8000, 8000, 3500], [6000  , 7000, 5000, 3500]]
    positions = [[4700, 8000, 8000, 6000]]
    for pos in positions:
        
        pwm0.duty_u16(pos[0])
        pwm1.duty_u16(pos[1])
        pwm2.duty_u16(pos[2])
        pwm3.duty_u16(pos[3])
        sleep(2)
positionServos()

while False:
     for position in range(3500,6000,50):
        pwm3.duty_u16(position)
        sleep(0.01)
     for position in range(6000,3500,-50):
        pwm3.duty_u16(position)
        sleep(0.01)   
    
while False:
    #pwm1.duty_u16(5000)
    for position in range(3000,6000,50):
        pwm2.duty_u16(position)
        sleep(0.01)
    for position in range(6000,3000,-50):
        pwm2.duty_u16(position)
        sleep(0.01)
    for position in range(1000,9000,50):
        pwm0.duty_u16(position)
        sleep(0.01)
    for position in range(9000,1000,-50):
        pwm0.duty_u16(position)
        sleep(0.01)
    for position in range(2000,6000,50):
        pwm1.duty_u16(position)
        sleep(0.01)
    for position in range(6000,2000,-50):
        pwm1.duty_u16(position)
        sleep(0.01)

        
#wm0.freq(0)
#wm1.freq(0)
#pwm2.freq(0)