# ChemBot
## Technical Project Description

### Story 
ChemBot is a great hardware robot …

To make any robot function, however, requires hardware and software. In this project, we are going to show how to set up a ChemBot robot with Rasperry Pi Pico W and Flask, in order to be able to control and manage your robot.

#### Outline
1. General description of setting up everything
2. Hardware setup
3. Software setup

#### Project Description
## 1. General description of setting up everything


## 2. Different prototype stages

The first prototype we created is the 3D model shown below. Two robot arms can be seen in the image of the project. On the right is the first physical prototype, however the correct function and angle setting did not work as desired. The one on the left is our final prototype, which contains five servo motors to get many angles. 

<img width="200" alt="Bildschirmfoto 2023-01-19 um 09 46 31" src="https://user-images.githubusercontent.com/83503396/213471994-934e0519-a25b-4381-9665-42536feb9e2f.png"> <img width="200" alt="Bildschirmfoto 2023-01-19 um 09 46 49" src="https://user-images.githubusercontent.com/83503396/213472020-e178e687-02d7-4d8c-a513-4a67835f532d.png"> <img width="200" alt="Bildschirmfoto 2023-01-19 um 09 47 04" src="https://user-images.githubusercontent.com/83503396/213472030-25b1861b-c1f0-4e7c-a692-5d55fc7413b7.png">

## 3. Hardware

### 3.1 Purchase list (recommendations)

* [<img src="https://user-images.githubusercontent.com/83503396/213228672-ed7b5c59-06e0-44ac-a893-a8ca0a4c9911.png" width="70"/>](https://user-images.githubusercontent.com/83503396/213228672-ed7b5c59-06e0-44ac-a893-a8ca0a4c9911.png)
Rasperry Pi Pico and USB cable: https://www.amazon.de/Raspberry-Pico-RPi-oder-Rasppishop/dp/B0B5GPSXX6/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3IU5U396SJOMQ&keywords=raspberry+pi+pico+w&qid=1669223804&sprefix=raspberry+pi+pico+w%2Caps%2C153&sr=8-3
* [<img src="https://user-images.githubusercontent.com/83503396/213222402-3cc18575-18cb-49a2-a40d-3136392fe67d.png" width="50"/>](https://user-images.githubusercontent.com/83503396/213222402-3cc18575-18cb-49a2-a40d-3136392fe67d.png) Servomotors: https://www.amazon.de/dp/B07KPS9845/ref=sspa_dk_detail_0?pd_rd_i=B07KPS9845&pd_rd_w=aAsjb&content-id=amzn1.sym.289b45a0-8ca0-4af2-9c85-5b0e57eb93c5&pf_rd_p=289b45a0-8ca0-4af2-9c85-5b0e57eb93c5&pf_rd_r=X7QVMN2B8A64BT1DVB58&pd_rd_wg=2Yez4&pd_rd_r=8100139d-5007-40e1-9164-e69768311cfd&s=toys&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw&th=1
* [<img src="https://user-images.githubusercontent.com/83503396/213229837-3eb164bb-0443-46fa-b397-9c035e16bf35.jpeg" width="50"/>](https://user-images.githubusercontent.com/83503396/213229837-3eb164bb-0443-46fa-b397-9c035e16bf35.jpeg)
Jumper cables: [https://www.amazon.de/AZDelivery-Jumper-Arduino-Raspberry-Breadboard/dp/B074P726ZR/ref=sr_1_1_sspa?ke
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
            
Stick the servo motors together with the wooden spatulas using the hot glue gun as shown in the picture. These can be trimmed with scissors as desired. Make sure that the small plate that is screwed onto the motors is adjusted so that the motors can still be turned correctly. When the five motors are glued together with the clamp, the lower transparent plate is glued to a larger wooden block for stabilization. Once everything is in place, as many wooden spatulas are attached and spread out so that you can see as little blue from the servo motors as you want to make it look nicer. If you want, you can also paint the wood.

[<img src="https://user-images.githubusercontent.com/83503396/213474640-d30029ef-7184-4b52-ad78-6b0ba6b3da1a.png" width="1000"/>](https://user-images.githubusercontent.com/83503396/213474640-d30029ef-7184-4b52-ad78-6b0ba6b3da1a.png)

#### 3.2.2 Connection between Rasperry Pi-Pico W and servomotors

After assembling the servo motors as robot arms, the ends will stick out. The Rasperry Pi Pico is connected to the five ends of the servo motors using the jumper cables and the breadboard as shown in the picture. While the black connections mean GND which stands for ground, the red connections of the servo motor with VCC are connected to +5V VBUS of the pi pico so that current flows.  On the other hand, the coloured connections from the servo motor called PWM (pulse-width modulation) to the GPIO pinout of the pi indicate that the servo motors can be controlled individually with information.

[<img src="https://user-images.githubusercontent.com/83503396/213477549-1b2939b2-7ef1-44f2-8016-9f453ea30eff.png" width="400"/>](https://user-images.githubusercontent.com/83503396/213477549-1b2939b2-7ef1-44f2-8016-9f453ea30eff.png)

#### 3.2.3 Create Fake Linkam station

We decided to build a Linkam stage as a mock-up, which is a device that ... . The reason for making a replica is that we couldn't be in the chemistry lab very often and that we didn't want to break anything on the real device with the first beginnings of our prototype. 

The mock-up is built approximately as shown in the 3D model in the picture. A hole was cut out of a square piece of wood with a hole saw, this piece is then glued to a very thin rectangular piece of wood, a cylinder about 2 cm in diameter is placed in the middle, which is painted black at the top so that the contrast between the sample and the background is greater for the camera. Glue aluminium foil for the optics into the resulting vacuum. Two bases are attached to the bottom of the dummy and a circle of magnets is placed in the middle to guide the rectangle holding the needle in a circle. In later stages of development, this also facilitates conductivity measurement.

[<img src="https://user-images.githubusercontent.com/83503396/213476176-ace465f1-d23b-4d7e-ae60-686cf26497b0.png" width="500"/>](https://user-images.githubusercontent.com/83503396/213476176-ace465f1-d23b-4d7e-ae60-686cf26497b0.png)

#### 3.3.4 Create height-adjustable stand for webcam

Um die Kamera in der richtigen Höhe über der Linkam Station zu befestigen und dadurch ein Mikroskop nachzuahmen wurde ein aufwendiger stand gebaut. Bei einem länglichen Stück Holz wird ein längliches Loch gesägt, daraufhin, Wird unten ein Winkel mit Schrauben angebracht und es auf ein großes dünnes Brett geschraubt, sodass es senkrecht steht. Die Kamera wird mit Schrauben auf ein anderes dünnes rechteckiges Brett geschraubt, an dieses Brett wird wiederum ein Winkel geschraubt. In den Winkel wird eine Schraube geschraubt, mit einem kleinen Holzzylinder dazwischen. Das wird verwendet um die Höhe zu verstellen, es kann fest geschraubt werden. Im unteren Teil des Winkels wird eine kleine Schraube mit dem Durchmessers des länglichen Lochs geschraubt, damit der Ständer mit der Kamera gerade adjustiert bleibt.

[<img src="https://user-images.githubusercontent.com/83503396/213476578-73508191-4e55-4b4c-89c2-fe37339ff569.png" width="150"/>](https://user-images.githubusercontent.com/83503396/213476578-73508191-4e55-4b4c-89c2-fe37339ff569.png)



