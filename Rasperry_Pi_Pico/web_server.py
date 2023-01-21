# Web_server includes all functions to set up the connection to the wifi, 
# to build the HTML code in the website and to control the servo motors.
# Run this file to perform Chembot's main function.

from time import sleep
from machine import Pin, PWM
import socket
import machine
import network
import html_code
import position_servos
import wifi_credentials

# Save positions user clicked
selected_positions = []

# Get wifi credentials # TODO fill out file
ssid, password = wifi_credentials.get_credentials()

#Connect to WLAN
def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print(wlan.ifconfig())
    ip = wlan.ifconfig()[0]
    # Show ip address to find website of Chembot
    print(f'Connected on {ip}')
    return ip

# Open a socket for website
def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

# Start a web server and handle interactions with website
def serve(connection):
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        print(request)
        selected_positions = position_servos.transform_request(request, selected_positions)
        html = html_code.getHTML(selected_positions)
        client.send(html)
        client.close()

# Start complete webserver
try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
    
except KeyboardInterrupt:
    machine.reset()


