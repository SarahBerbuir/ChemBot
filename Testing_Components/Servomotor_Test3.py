# Test servomotor positions: Position one servomotor, test each one at one time
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
