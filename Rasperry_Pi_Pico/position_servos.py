
# After clicking on Start this function is executed. 
# It starts animation of robot arm and changes from start_pos to pos

from machine import Pin, PWM
import machine
from time import sleep

#Initializing Pins of Raspberry Pi Pico W
pwm0 = PWM(Pin(0))
pwm2 = PWM(Pin(1))
pwm1 = PWM(Pin(2))
pwm3 = PWM(Pin(3))
pwm4 = PWM(Pin(4))

# Frequence of 50 for servomotors
pwm0.freq(50)
pwm1.freq(50)
pwm2.freq(50)
pwm3.freq(50)
pwm4.freq(50)

# Save positions for transformation of servomotors
startPosition0 = [5500,3600,4000,5000,6500]
position0 = [4400, 3600, 4000, 5000, 3500]
startPosition1 = [4400, 3600, 4000, 5000, 3500]
position1 = [4400, 3800, 5000, 5000, 1000]

def startAnalysis(start_pos, pos):
    pwm0.duty_u16(start_pos[0])
    pwm1.duty_u16(start_pos[1])
    pwm2.duty_u16(start_pos[2])
    pwm3.duty_u16(start_pos[3])
    pwm4.duty_u16(start_pos[4])
    sleep(2)
    pwm0.duty_u16(pos[0])
    pwm1.duty_u16(pos[1])
    pwm2.duty_u16(pos[2])
    pwm3.duty_u16(pos[3])
    pwm4.duty_u16(pos[4])    

# Transform request and handle interactions of start and reset button    
def transform_request(request, selected_positions):
    try:
        request = request.split()[1]
        if  request[1] == "(":
            if len(selected_positions)==2:
                selected_positions.clear() 
            row = request[2]
            col = request[4]
            request = request[2:-2]
            item = [int(row), int(col)]
            if not item in selected_positions:
                selected_positions.append(item)
        print(selected_positions)
    except IndexError:
        pass
    print(request)
    if request == '/startAnalysis?':
        print("start")
        if selected_positions[0][1] >= 4:
            startAnalysis(startPosition0, position0) 
        else:
            startAnalysis(startPosition1, position1) 
    elif request == '/resetSelection?':
        print("reset")
        selected_positions.clear()   
    return selected_positions
