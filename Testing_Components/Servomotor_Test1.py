from machine import Pin,PWM
from time import sleep

MIN_Position = 5200
MID_Position = 4400
MAX_Position = 4400

servo = PWM(Pin(0))
servo.freq(50)
servo.duty_u16(4400)

servo1 = PWM(Pin(1))
servo1.freq(50)
servo1.duty_u16(3600)

servo2 = PWM(Pin(2))
servo2.freq(50)
servo2.duty_u16(4000)

servo3 = PWM(Pin(3))
servo3.freq(50)
servo3.duty_u16(5000)

servo4 = PWM(Pin(4))
servo4.freq(50)
servo4.duty_u16(3000)

while False:
    print("Test")
    servo.duty_ns(MIN_Position)
    sleep(2)
    servo.duty_ns(MID_Position)
    sleep(2)
    servo.duty_ns(MAX_Position)
    sleep(2)

while True:
    print("Test")
    #servo.duty_u16(MIN_Position)
    servo4.duty_u16(3000)
    servo2.duty_u16(4000)
    servo1.duty_u16(3600)
    servo.duty_u16(4400)
    sleep(2)
    #servo.duty_u16(MID_Position)
    sleep(2)
    #servo.duty_u16(MAX_Position)
    servo4.duty_u16(1000)
    servo2.duty_u16(5000)
    servo1.duty_u16(3300)
    servo.duty_u16(4400)

    sleep(2)

