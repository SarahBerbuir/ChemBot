from time import sleep
from machine import Pin, PWM

pwm0 = PWM(Pin(0))
pwm1 = PWM(Pin(1))
pwm2 = PWM(Pin(2))
pwm3 = PWM(Pin(3))

pwm0.freq(50)
pwm1.freq(50)
pwm2.freq(50)
pwm3.freq(50)

MIN_Position = 1000000
MID_Position = 1500000
MAX_Position = 2000000

pwm2.duty_ns(MIN_Position)
pwm0.duty_ns(MIN_Position)
pwm1.duty_ns(MIN_Position)
pwm3.duty_ns(MIN_Position)

while False:
    for position in range(MIN_Position,MAX_Position,50):
        pwm1.duty_u16(position)
        sleep(0.01)
    for position in range(MAX_Position,MIN_Position,-50):
        pwm1.duty_u16(position)
        sleep(0.01)
    for position in range(MIN_Position,MAX_Position,50):
        pwm2.duty_u16(position)
        sleep(0.01)
    for position in range(MAX_Position,MIN_Position,-50):
        pwm2.duty_u16(position)
        sleep(0.01)
    for position in range(MIN_Position,MAX_Position,50):
        pwm0.duty_u16(position)
        sleep(0.01)
    for position in range(MAX_Position,MIN_Position,-50):
        pwm0.duty_u16(position)
        sleep(0.01)
    for position in range(MIN_Position,MAX_Position,50):
        pwm3.duty_u16(position)
        sleep(0.01)
    for position in range(MAX_Position,MIN_Position,-50):
        pwm3.duty_u16(position)
        sleep(0.01)


pwm0.freq(0)
#pwm1.freq(0)
pwm2.freq(0)
