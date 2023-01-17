from time import sleep
from machine import Pin, PWM
import socket
from picozero import pico_temp_sensor, pico_led
import machine
import network
import html_code
import position_servos
import wifi_credentials

pwm0 = PWM(Pin(0))
pwm2 = PWM(Pin(1))
pwm1 = PWM(Pin(2))
pwm3 = PWM(Pin(3))
pwm4 = PWM(Pin(4))

pwm0.freq(50)
pwm1.freq(50)
pwm2.freq(50)
pwm3.freq(50)
pwm4.freq(50)

already_started = False
selected_positions = []

startPosition0 = [5500,3600,4000,5000,6500]
position0 = [4400, 3600, 4000, 5000, 3500]
startPosition1 = [4400, 3600, 4000, 5000, 3500]
position1 = [4400, 3800, 5000, 5000, 1000]


ssid, password = wifi_credentials.get_credentials()



def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print(wlan.ifconfig())
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    
    return ip

def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def startAnalysis1(start_pos, pos):
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
    
        
def serve(connection):
    #Start a web server
    state = 'OFF'
    pico_led.off()
    temperature = 0
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        print(request)
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
        

            if selected_positions[0][1] >= 4:
                startAnalysis1(startPosition0, position0) 
            else:
                startAnalysis1(startPosition1, position1) 
        elif request == '/resetSelection?':
            print("reset")
            selected_positions.clear() 

        state = selected_positions
        temperature = pico_temp_sensor.temp
        html = html_code.getHTML(state)
        client.send(html)
        client.close()
    
try:

    ip = connect()
    connection = open_socket(ip)
    serve(connection)
    
except KeyboardInterrupt:
    machine.reset()


