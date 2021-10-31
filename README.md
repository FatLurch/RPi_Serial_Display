# RPi_Serial_Display
 
This simple Python script displays messages recieved on the Serial bus to the Shell window

This is the first time I've ever used a Raspberry Pi so the code will be *rough*. I'd love any help/suggestions anyone has to offer!

![Serial_Read](http://tsog-milsim.com/images/ARMACOM_RaspberryPi_sm.png)

This script can be tested with the LCD mission for ARMA: https://github.com/FatLurch/TEST_ARMACOM_LCD.vr

 ## Wiring:
 **Important:** Be sure the serial adapter you use is configured for 3.3 volt signals, *not* 5 volts (your board could be damaged otherwise)
 
 I used an FTDI adapter (FT232) like this one on Amazon (Affiliate Link): https://amzn.to/2Y5IEdi

![Wiring](http://tsog-milsim.com/images/ARMACOM_RaspberryPi_Wiring.png)

---

Alternatively, you can use the Serial on an Arduino to drive the Rasperry Pi - you **will** need a logic level shifter to drop the 5 volt signals from the Arduino down to 3.3 volts for the Raspberry Pi.

Affiliate Link for the Level Shifter on Amazon: https://amzn.to/3mwmdaE

![Alt Wiring](http://tsog-milsim.com/images/Pi_from_Arduino.png)
