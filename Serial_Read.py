#!/usr/bin/env python
import time
import serial
import unicodedata
ser = serial.Serial(
port='/dev/serial0',
baudrate = 9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
)


while 1:
    x=ser.readline()
    print(x)