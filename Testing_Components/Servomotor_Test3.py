from machine import Pin,PWM
from time import sleep

MIN_Position = 3000
MID_Position = 3000
MAX_Position = 5000

servo = PWM(Pin(3))
servo.freq(50)
servo.duty_ns(MID_Position)

while True:
    print("Test")
    servo.duty_u16(MIN_Position)
    sleep(2)
    servo.duty_u16(MID_Position)
    sleep(2)
    servo.duty_u16(MAX_Position)
    sleep(2)

while False:
    print("Test")
    for position in range(MIN_Position,MAX_Position,50):
        servo.duty_u16(position)
        sleep(0.01)
    for position in range(MAX_Position,MIN_Position,-50):
        servo.duty_u16(position)
        sleep(0.01)


