# ChemBot - Technical Project Description (TPD)

## Story 
<img width="238" alt="Logo" src="https://user-images.githubusercontent.com/83503396/213694473-d35c9208-7573-4f5b-9f8c-4f88c4ed014b.png">

ChemBot is a hardware robotic arm designed to automate laboratory processes, specifically for electrochemistry researchers. Our solution is made up of two robotic arms, an adjustable webcam, and a user-friendly web application, and it is designed to assist researchers with the painful and time-consuming tasks they face on a daily basis. The robot arm moves needles to predefined certain points on the sample, making it a specialized solution for solid-state battery research. The solution is highly flexible, so it can also be used in different research areas with minimal modification.
Any robot, however, requires both hardware and software to function. In this project, we will demonstrate how to configure a ChemBot robot with a Raspberry Pi Pico W and Flask in order to control and manage your robot.

## Outline
1. General description
2. Different prototype stages
3. Hardware setup

    3.1 Purchase list
    
    3.2 Step-by-step-setup

    3.2.1 Create robot arms

    3.2.2 Connection between Raspberry Pi-Pico W and servomotors

    3.2.3 Create Fake Linkam station

    3.3.4 Create height-adjustable stand for webcam

4. Software

    4.1 Short overview of repository code structure

    4.2 Webserver of webcam using flask

    4.3 Optional: Test servomotors without Wifi

    4.4 Webserver of Raspberry Pi Pico W

    4.4.1 Explanation of used libraries

    4.4.2 Setup webserver

5. Setup of all components

### Project Description
## 1. General description
ChemBot consists of both hardware and software components. On the hardware side for rebuilding the prototype, there is a robot arm, a mock-up Linkam Stage, and a webcam connected to the laptop via USB. The software side consists of the code for the webcam's web server and a Raspberry Pi Pico W web server, which controls the servo motors.

## 2. Different prototype stages

The 3D model shown below is the first prototype we created, the second and third one can be seen in the other image. The first physical prototype is shown on the right, but the correct function and angle setting did not work as expected. The one on the left is our final prototype, which has five servo motors to achieve a wide range of angles.

<img width="200" alt="Bildschirmfoto 2023-01-19 um 09 46 31" src="https://user-images.githubusercontent.com/83503396/213471994-934e0519-a25b-4381-9665-42536feb9e2f.png"> <img width="200" alt="Bildschirmfoto 2023-01-19 um 09 46 49" src="https://user-images.githubusercontent.com/83503396/213472020-e178e687-02d7-4d8c-a513-4a67835f532d.png"> <img width="200" alt="Bildschirmfoto 2023-01-19 um 09 47 04" src="https://user-images.githubusercontent.com/83503396/213472030-25b1861b-c1f0-4e7c-a692-5d55fc7413b7.png">
[<img src="https://user-images.githubusercontent.com/83503396/213709492-51242568-d4b1-44fb-b990-2007aba6f61c.jpeg" width="600"/>](https://user-images.githubusercontent.com/83503396/213709492-51242568-d4b1-44fb-b990-2007aba6f61c.jpeg)

## 3. Hardware

### 3.1 Purchase list (recommendations)

* [<img src="https://user-images.githubusercontent.com/83503396/213228672-ed7b5c59-06e0-44ac-a893-a8ca0a4c9911.png" width="70"/>](https://user-images.githubusercontent.com/83503396/213228672-ed7b5c59-06e0-44ac-a893-a8ca0a4c9911.png)
Raspberry Pi Pico and USB cable: https://www.amazon.de/Raspberry-Pico-RPi-oder-Rasppishop/dp/B0B5GPSXX6/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3IU5U396SJOMQ&keywords=raspberry+pi+pico+w&qid=1669223804&sprefix=raspberry+pi+pico+w%2Caps%2C153&sr=8-3
* [<img src="https://user-images.githubusercontent.com/83503396/213222402-3cc18575-18cb-49a2-a40d-3136392fe67d.png" width="50"/>](https://user-images.githubusercontent.com/83503396/213222402-3cc18575-18cb-49a2-a40d-3136392fe67d.png) Servomotors: https://www.amazon.de/dp/B07KPS9845/ref=sspa_dk_detail_0?pd_rd_i=B07KPS9845&pd_rd_w=aAsjb&content-id=amzn1.sym.289b45a0-8ca0-4af2-9c85-5b0e57eb93c5&pf_rd_p=289b45a0-8ca0-4af2-9c85-5b0e57eb93c5&pf_rd_r=X7QVMN2B8A64BT1DVB58&pd_rd_wg=2Yez4&pd_rd_r=8100139d-5007-40e1-9164-e69768311cfd&s=toys&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw&th=1
* [<img src="https://user-images.githubusercontent.com/83503396/213229837-3eb164bb-0443-46fa-b397-9c035e16bf35.jpeg" width="50"/>](https://user-images.githubusercontent.com/83503396/213229837-3eb164bb-0443-46fa-b397-9c035e16bf35.jpeg)
Jumper cables: [https://www.amazon.de/AZDelivery-Jumper-Arduino-Raspberry-
oard/dp/B074P726ZR/ref=sr_1_1_sspa?ke
ywords=jumper%2Bkabel&qid=1669231300&sprefix=jumper%2B%2Caps%2C104&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&smid=A1X7QLRQH87QA3&th=1](https://www.amazon.de/dp/B074P726ZR?psc=1&ref=ppx_yo2ov_dt_b_product_details)
* [<img src="https://user-images.githubusercontent.com/83503396/213225906-fd1136a6-14c4-4ccb-bc25-e5a2b160928d.png" width="50"/>](https://user-images.githubusercontent.com/83503396/213225906-fd1136a6-14c4-4ccb-bc25-e5a2b160928d.png) Breadboards: https://www.amazon.de/AZDelivery-Breadboard-Steckbrett-Kontakten-Arduino/dp/B078JJJ2SJ/ref=sr_1_4?keywords=steckbrett&qid=1669231268&sr=8-4
* [<img src="https://user-images.githubusercontent.com/83503396/213225634-7655a353-6dd7-4edb-95c1-626eb5136a64.png" width="50"/>](https://user-images.githubusercontent.com/83503396/213225634-7655a353-6dd7-4edb-95c1-626eb5136a64.png) Wooden spatula: https://www.amazon.de/gp/product/B004ULKBLI/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&psc=1
* [<img src="https://user-images.githubusercontent.com/83503396/213228510-bca104c5-b183-449e-b997-f2e7069d0747.png" width="35"/>](https://user-images.githubusercontent.com/83503396/213228510-bca104c5-b183-449e-b997-f2e7069d0747.png) Clamps: https://www.amazon.de/gp/product/B08MQ1Y6FK/ref=ppx_yo_dt_b_asin_title_o00_s01?ie=UTF8&psc=1
* [<img src="https://user-images.githubusercontent.com/83503396/213230727-a60176d8-5ef6-44d2-8912-b514826c3f14.jpg" width="50"/>](https://user-images.githubusercontent.com/83503396/213230727-a60176d8-5ef6-44d2-8912-b514826c3f14.jpg) USB Webcam: https://www.amazon.de/dp/B087YLG27N?psc=1&ref=ppx_yo2ov_dt_b_product_details
* [<img src="https://user-images.githubusercontent.com/83503396/213230652-2db8b136-c794-4285-b568-5fdb859e556b.jpg" width="50"/>](https://user-images.githubusercontent.com/83503396/213230652-2db8b136-c794-4285-b568-5fdb859e556b.jpg) Magnets: https://www.amazon.de/dp/B0BJPS5GMH?psc=1&ref=ppx_yo2ov_dt_b_product_details

Tools:
* Wood (A larger wooden plate, two blocks for the robot arms, various elongated pieces of wood for the camera tripod and two angles)
* Screws
* [<img src="https://user-images.githubusercontent.com/83503396/213231855-e202f88f-87c1-475e-ac34-30dac68c10d3.jpeg" width="50"/>](https://user-images.githubusercontent.com/83503396/213231855-e202f88f-87c1-475e-ac34-30dac68c10d3.jpeg) Heat glue gun
* Workshop tools: Band saw, hole saw, disc sander, spindle sander, turning lathe, cordless screwdriver

   
### 3.2 Step-by-step-setup

#### 3.2.1 Create robot arms (step by step image)
            
Using the hot glue gun, adhere the servo motors to the wooden spatulas as shown in the picture. These can be trimmed as desired with scissors. Make sure that the small plate that is screwed onto the motors is properly adjusted so that the motors can still be turned. When the five motors are glued together with the clamp, the lower transparent plate is glued to a larger wooden block for stabilization. Once everything is in place, attach and spread out as many wooden spatulas as you want to see as little blue from the servo motors as possible to make it look nicer. You can also paint the wood if you want.

[<img src="https://user-images.githubusercontent.com/83503396/213474640-d30029ef-7184-4b52-ad78-6b0ba6b3da1a.png" width="1000"/>](https://user-images.githubusercontent.com/83503396/213474640-d30029ef-7184-4b52-ad78-6b0ba6b3da1a.png)
[<img src="https://user-images.githubusercontent.com/83503396/213696975-d7d3f8ef-049a-4b74-93c6-9dde50b23b8b.jpeg" width="500"/>](https://user-images.githubusercontent.com/83503396/213696975-d7d3f8ef-049a-4b74-93c6-9dde50b23b8b.jpeg)

#### 3.2.2 Connection between Raspberry Pi-Pico W and servomotors

The ends of the servo motors will protrude after they are assembled as robot arms. The Raspberry Pi Pico is a low-cost, high-performance microcontroller board with numerous digital interface options. It’s connected to the five ends of the servo motors via jumper cables and a breadboard, as shown in the picture. While the black connections represent GND (ground), the red connections of the servo motor with VCC are connected to the +5V VBUS of the pi pico to allow current to flow. The coloured connections from the servo motor, called PWM (pulse-width modulation) to the GPIO pinout of the pi, on the other hand, indicate that the servo motors can be controlled individually with information.

[<img src="https://user-images.githubusercontent.com/83503396/213477549-1b2939b2-7ef1-44f2-8016-9f453ea30eff.png" width="500"/>](https://user-images.githubusercontent.com/83503396/213477549-1b2939b2-7ef1-44f2-8016-9f453ea30eff.png)
[<img src="https://user-images.githubusercontent.com/83503396/213696894-d1187ff8-d947-4cb0-a306-8b5b95dd20b6.jpeg" width="500"/>](https://user-images.githubusercontent.com/83503396/213696894-d1187ff8-d947-4cb0-a306-8b5b95dd20b6.jpeg)

#### 3.2.3 Create Fake Linkam station

We decided to build a Linkam stage as a model, the stage is usually used for specific research applications such as semiconductor materials, which is used in many laboratories. The reasons for making a replica is that we couldn't be in the chemistry lab very often and that we didn't want to break anything on the real device with the early stages of our prototype.

The mock-up is constructed approximately in the manner depicted in the 3D model in the picture. With a hole saw, a hole was cut out of a square piece of wood, which was then glued to a very thin rectangular piece of wood, and a cylinder about 2 cm in diameter was placed in the middle, which was painted black at the top to increase the contrast between the sample and the background for the camera. Glue aluminium foil for the optics into the resulting vacuum. Two bases are attached to the bottom of the dummy and a circle of magnets is placed in the middle to guide the rectangle holding the needle in a circle. This also facilitates conductivity measurement in later stages of development.

[<img src="https://user-images.githubusercontent.com/83503396/213476176-ace465f1-d23b-4d7e-ae60-686cf26497b0.png" height="250"/>](https://user-images.githubusercontent.com/83503396/213476176-ace465f1-d23b-4d7e-ae60-686cf26497b0.png)
[<img src="https://user-images.githubusercontent.com/83503396/213695361-c5925c17-aedf-42a0-9b8b-fbcf3d3474ba.jpeg" height="250"/>](https://user-images.githubusercontent.com/83503396/213695361-c5925c17-aedf-42a0-9b8b-fbcf3d3474ba.jpeg)
[<img src="https://user-images.githubusercontent.com/83503396/213695705-da2917ee-b9a9-4543-a57d-bb2adb3e15e1.jpeg" height="250"/>](https://user-images.githubusercontent.com/83503396/213695705-da2917ee-b9a9-4543-a57d-bb2adb3e15e1.jpeg)

Also, glue three small pieces of wooden spatulas together, stick a paper clip on the top to represent the needle and stick a magnet on the bottom. 

[<img src="https://user-images.githubusercontent.com/83503396/213696742-03dd7ea7-ec3c-461a-83bd-6d4cc38d7ae1.png" height="80"/>](https://user-images.githubusercontent.com/83503396/213696742-03dd7ea7-ec3c-461a-83bd-6d4cc38d7ae1.png)

#### 3.3.4 Create height-adjustable stand for webcam
In order to mount the camera at the right height above the Linkam station and thus imitate a microscope, an elaborate stand was built. Cut an elongated hole in an elongated piece of wood, attach an angle block with screws at the bottom and screw it to a large thin board so that it stands vertically. The camera is screwed onto another thin rectangular board, and an angle block is fixed to this board. A screw is placed in the angle with a small wooden cylinder in between. This is used to adjust the height, it can be tightened. A small screw with the diameter of the oblong hole is inserted in the lower part of the angle block so that the stand with the camera remains adjusted.

[<img src="https://user-images.githubusercontent.com/83503396/213476578-73508191-4e55-4b4c-89c2-fe37339ff569.png" width="200"/>](https://user-images.githubusercontent.com/83503396/213476578-73508191-4e55-4b4c-89c2-fe37339ff569.png)
[<img src="https://user-images.githubusercontent.com/83503396/213714129-ca4dd4e5-0db2-4186-8753-ebbb51050ff0.png" width="350"/>](https://user-images.githubusercontent.com/83503396/213714129-ca4dd4e5-0db2-4186-8753-ebbb51050ff0.png)

## 4. Software

### 4.1 Short overview of repository code structure
    
`Local_webserver` contains code to set up a webserver that cropps and transfers the images from the webcam, `Rasperry_Pi_Pico` contains all the code to run the ChemBot website on the Rasperry Pi Pico W to control the servo motors. `Testing_Components` contains optional files that can help to test the servo motors and their interaction before setting up all the components.
    
### 4.2 Short overview of GitHub code structureWebserver of webcam using flask
    
In order to display the webcam image correctly on the ChemBot website, an extra web server is set up with the help of Flask, OpenCV is used to get the camera images and transform them.

| Name         | Usage                             | Link                                    |
| ------------ | --------------------------------- | --------------------------------------- |
|[<img src="https://user-images.githubusercontent.com/83503396/213694242-ee8c5071-e070-492a-a0d5-5c39d1adfaef.png" width="60"/>](https://user-images.githubusercontent.com/83503396/213694242-ee8c5071-e070-492a-a0d5-5c39d1adfaef.png) flask      | Python web framework with useful tools and functions that facilitate the creation of web applications in Python.                   | https://flask.palletsprojects.com/en/2.2.x/|
| [<img src="https://user-images.githubusercontent.com/83503396/213694260-6f6c6454-2d1d-49e4-a969-a74292163925.jpg" width="50"/>](https://user-images.githubusercontent.com/83503396/213694260-6f6c6454-2d1d-49e4-a969-a74292163925.jpg) cv2      | OpenCV is a free program library with algorithms for image processing and computer vision. It is written for the programming languages C, C++, Python and Java and is available as free software under the terms of the Apache 2 License.                   | https://opencv.org/|
    
Install `pip3 install flask`  and  `pip3 install opencv-python`.
    
After executing the file `app.py` the image of the camera can now be accessed under `http://127.0.0.1:8000/`. 
    
### 4.3 Optional: Test servomotors without Wifi
    
There are several files under `Testing_Components` that can help to test either individual servo motors `(Servomotor_Test3.py)` or the interaction of all servo motors.
    
### 4.4 Webserver of Raspberry Pi Pico W

#### 4.4.1 Explanation of used libraries
    
For Setup of Raspberry Pi Pico W MicroPython was used and die module untendrunter.
| Name         | Usage                             | Link                                    |
| ------------ | --------------------------------- | --------------------------------------- |
| network      | The network module is used to configure the WiFi connection                   | [https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html](https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html)|
| socket         | This module provides access to the BSD socket interface.                         | [https://docs.micropython.org/en/latest/library/socket.html](https://docs.micropython.org/en/latest/library/socket.html)                                 |
| machine         | This module contains specific functions related to the hardware on a particular board. Most functions in this module allow to achieve direct and unrestricted access to and control of hardware blocks on a system                         | [https://docs.micropython.org/en/latest/library/machine.html](https://docs.micropython.org/en/latest/library/machine.html)                      |
| time       | This module provides functions for getting the current time and date, measuring time intervals, and for delays.          | [https://docs.micropython.org/en/latest/library/time.html](https://docs.micropython.org/en/latest/library/time.html) | 
    
#### 4.4.2 Setup webserver
    
##### Get Thonny IDE
Download the Thonny IDE https://thonny.org/ and install it. Thonny is an integrated development environment for Python, recommended by the Raspberry Pi Foundation.
    
##### Set up MicroPython on Raspberry Pi Pico W
    
Basic steps of getting your Raspberry Pi Pico running with MicroPython. Follow these steps if you have a new Raspberry Pi Pico or you want to change a Pi Pico that is not currently setup for MicroPython.

1. Download the MicroPython firmware image: https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2
2. Connect a Micro USB cable to your Pi Pico. But, do not yet con- nect it to your computer.
3. Push and hold the button labeled "BOOTSEL"
4. Connect the Pi Pico to your computer by plugging in the USB cable. You can now release the button.
5. The Pi Pico will mount as a mass storage device (RPI-RP2)
6. Copy the MicroPython image (Step 1) onto RPI-RP2
7. Once completed, your Pi Pico reboots automatically and disap- pears from the list of mass storage devices. The microcontroller is now running MicroPython, congratulations! You can now interact with the Pi Pico through USB Serial.
8. Find the corresponding serial port (On Windows: Check the Device Manager (Ports COM & LPT)))
9. Connect to this serial line with and go to Run --> Select Interpreter and choose MicoPython (Rasoerry Pi Pico). Select the corresponding COM port or try automatic detection
    
Now the Raspberry Pi Pico W is successfully setup for use with MicroPython
    
First add your ssid and wifi password in file `wifi_credentials.py`. Run web_server.py and test it on im Terminal angegebenen Port.

##### HTML code
    
The file `html_code.py` shows an HTML code that is formatted correctly at first. In the last lines of the function there, unnecessary spaces and paragraphs are removed, as the Raspberry Pi Pico W cannot display so much information. This is also the reason why the user interface was kept very simple. For usability, a header with logo is displayed, as well as a short introduction text. Moreover, there is a table positioned above the image of the webcam, which is fetched from the web server mentioned above. There is also a text line indicating which parts of the table have been clicked. Two buttons, Start and Reset, are available for activating the robot or resetting the previously selected values.

## 5. Setup of all components
    
The hardware is in place, the web server of the webcam is set up, the web server of the Raspberry Pi Pico W is running. To access the web interface of ChemBot, it is important to look at the terminal of the Thonny IDE (after running `web_server.py`). There you can see the port number, enter it into a browser. Now the page should be visible there. In the box of the table, you should see the picture of the webcam. 

[<img src="https://user-images.githubusercontent.com/83503396/213697155-a7a60bb3-d876-4358-b34e-f31e8dbdc834.jpeg" width="500"/>](https://user-images.githubusercontent.com/83503396/213697155-a7a60bb3-d876-4358-b34e-f31e8dbdc834.jpeg)

To operate it, one or two (in the implementation only the first one is important, the second one is meant for a possible second connected robot arm) of the table points are now clicked. Once the robot is correctly positioned in the joint of the Linkam station, `Start` is clicked. Now the robot guides the needle to the desired location on the sample.


